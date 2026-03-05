#!/usr/bin/env python3
"""
Document Converter Script
Converts source documents to Markdown using markitdown.
Strictly enforces repository boundary - will NOT create files outside repo root.
"""

import sys
import subprocess
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {'.docx', '.pptx', '.xlsx', '.pdf', '.md', '.txt', '.png', '.jpg', '.jpeg', '.gif'}


def find_repo_root() -> Path:
    """Find repository root by locating workflow.md"""
    current = Path.cwd()
    
    for parent in [current] + list(current.parents):
        workflow_path = parent / 'WORKFLOW.md'
        if workflow_path.exists():
            return parent
    
    raise RuntimeError("ERROR: workflow.md not found. Run from project root.")


def is_within_repo(file_path: Path, repo_root: Path) -> bool:
    """Verify a path is within repository root (no path traversal)"""
    try:
        resolved = file_path.resolve()
        resolved_root = repo_root.resolve()
        return resolved.resolve().is_relative_to(resolved_root)
    except (ValueError, OSError):
        return False


def get_output_path(input_path: Path, source_dir: Path, output_root: Path, repo_root: Path) -> Path:
    """Calculate output path preserving folder structure"""
    relative_path = input_path.relative_to(source_dir)
    output_path = output_root / relative_path.with_suffix('.md')
    
    if not is_within_repo(output_path, repo_root):
        raise ValueError(f"Output path would be outside repo: {output_path}")
    
    return output_path


def convert_file(input_file: Path, output_file: Path, timeout: int = 30) -> tuple[bool, str]:
    """Convert single file using markitdown via Python module. Returns (success, error_message)"""
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        result = subprocess.run(
            [sys.executable, '-m', 'markitdown', str(input_file), '-o', str(output_file)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=input_file.parent.parent
        )
        
        if result.returncode == 0:
            return True, ""
        else:
            return False, result.stderr.strip() or result.stdout.strip()
            
    except subprocess.TimeoutExpired:
        return False, f"Timeout ({timeout}s) - file may be corrupted or too large"
    except FileNotFoundError:
        return False, "Python or markitdown not found - ensure venv is activated and markitdown[all] is installed"
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    logger.info("Starting document conversion...")
    
    try:
        repo_root = find_repo_root()
        logger.info(f"Repository root: {repo_root}")
    except RuntimeError as e:
        logger.error(str(e))
        sys.exit(1)
    
    source_dir = repo_root / 'documents' / 'source'
    output_dir = repo_root / 'documents' / 'processed'
    error_log = repo_root / 'documents' / 'processed' / 'error_log.md'
    
    if not source_dir.exists():
        logger.error(f"Source directory not found: {source_dir}")
        sys.exit(1)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    files_to_convert = []
    for ext in SUPPORTED_EXTENSIONS:
        files_to_convert.extend(source_dir.rglob(f'*{ext}'))
        files_to_convert.extend(source_dir.rglob(f'*{ext.upper()}'))
    
    if not files_to_convert:
        logger.info("No files to convert.")
        return
    
    logger.info(f"Found {len(files_to_convert)} files to convert")
    
    results = []
    errors = []
    
    for input_file in sorted(files_to_convert):
        if not is_within_repo(input_file, repo_root):
            logger.warning(f"SKIPPED (outside repo): {input_file}")
            continue
        
        output_file = get_output_path(input_file, source_dir, output_dir, repo_root)
        
        logger.info(f"Converting: {input_file.name} -> {output_file.name}")
        
        success, error = convert_file(input_file, output_file)
        
        if success:
            results.append(f"- {input_file.name} -> {output_file.name}")
        else:
            errors.append(f"| {input_file.name} | {error} |")
            logger.warning(f"Failed: {input_file.name} - {error}")
    
    error_content = [
        "# Conversion Error Log",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        "| Filename | Error |",
        "|----------|-------|",
    ] + errors
    
    error_log.write_text('\n'.join(error_content))
    
    summary = [
        "# Conversion Results",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"Total files: {len(files_to_convert)}",
        f"Successful: {len(results)}",
        f"Failed: {len(errors)}",
        f"",
        "## Converted Files",
        "",
    ] + results + ["", "## Errors", f"See error_log.md ({len(errors)} failures)"]
    
    results_file = output_dir / 'conversion_results.md'
    results_file.write_text('\n'.join(summary))
    
    logger.info(f"Conversion complete: {len(results)} succeeded, {len(errors)} failed")
    logger.info(f"Results: {results_file}")
    logger.info(f"Errors: {error_log}")


if __name__ == '__main__':
    main()
