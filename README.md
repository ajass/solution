# Solution Architect Workflow

Minimal workflow for Solution Architects to convert documents and manage architecture artifacts.

## What's Included

- `WORKFLOW.md` - Full workflow definition (7 phases)
- `scripts/convert_artifacts.py` - Document converter script

## Quick Start

```powershell
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Phase 1 will create the folder structure automatically

# When ready for Phase 3, run:
cd scripts
python -m venv venv
.\venv\Scripts\Activate.ps1
.\venv\Scripts\pip.exe install "markitdown[all]"
.\venv\Scripts\python.exe scripts/convert_artifacts.py
```

## Requirements

- Windows 11
- VSCode
- GitHub Copilot
- Python 3.11+

## Workflow

See `WORKFLOW.md` for the full 7-phase workflow:
1. File Structure Proposal (creates folders)
2. Source File Collection
3. Document Conversion
4. Template Verification
5. Content Mapping & Completeness Analysis
6. Documentation Update
7. Summary
