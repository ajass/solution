# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Folder structure fix: created artifacts/, documents/source, documents/processed, scripts/
- Workflow streamlined: added 4 milestone checkpoints instead of 7 phase confirmations
- Workflow updated: templates created in Phase 1, verified in Phase 4
- Phase 3: detailed error reporting with filename, error type, suggested fix
- Phase 5 loop: simplified to re-run only conversion + mapping (not full workflow)
- Governance Rules: added milestone checkpoint requirement
- Pre-built convert_artifacts.py script (eliminates AI code generation issues)

### Changed
- Phase 3: Uses pre-built script instead of AI-generated code
- Strict path enforcement: verify repo root first, abort if outside boundary
- Guardrails: added explicit abort conditions for path violations
- Phase 3: Added venv setup verification step before conversion
- Script: removed unnecessary cwd parameter
- Script: added pre-flight check for markitdown before conversion starts
- `/artifacts/discovered/` folder for unmapped content
- `unmapped-content.md` template for tracking unmatched content
- Content Mapping Strategy section in WORKFLOW.md
- Completeness report now tracks discovered/unmapped items

### Changed
- Phase 3 creates discovered/ folder and unmapped-content.md template
- Folder structure in WORKFLOW.md and README.md updated

### Fixed
- Workflow phase ordering: Convert documents first, then create templates
- Phase 1 now scaffolds folder structure after user approval
- Phase 2 includes explicit reminder to add source files to /documents/source
- Conversion script uses subprocess to call markitdown CLI (not Python module)
- Conversion script installs `markitdown[all]` before attempting conversions
- Added folder verification step before conversion in Phase 3
- Added repository boundary enforcement to prevent files outside root
- Moved Copilot Bootstrap Prompt to top of WORKFLOW.md for quick access
- Added dynamic repo root discovery in Phase 1 (finds workflow.md to determine root)
- Added dynamic repo root discovery in Phase 3 (ensures all paths relative to discovered root)

### Removed
- (none)

## [v0.1.0] - YYYY-MM-DD

### Added
- Initial release with 7-phase workflow
- Template files (requirements, architecture, diagrams, ADR)
- README.md and CHANGELOG.md
- .gitignore
