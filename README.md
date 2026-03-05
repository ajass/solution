# Solution Architect Workflow

Minimal workflow for Solution Architects to convert documents and manage architecture artifacts.

## What's Included

- `WORKFLOW.md` - Full workflow definition (7 phases) with embedded converter script

## Quick Start

```powershell
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Phase 1 creates folders and the converter script automatically

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

See `WORKFLOW.md` for the full 7-phase workflow. The converter script is embedded in WORKFLOW.md and created during Phase 1.
