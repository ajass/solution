# Solution Architect Project

A professional workflow for Solution Architects to manage architecture artifacts, convert documents to Markdown, and maintain governance standards.

## Overview

This project provides a structured workflow for Solution Architects to:
- Organize architecture folder structure
- artifacts in a standardized Convert documents (docx, pptx, xlsx, pdf, images) to Markdown
- Populate templates with converted content
- Analyze template completeness
- Maintain documentation through README and CHANGELOG discipline

## Folder Structure

```
/
├── artifacts/
│   ├── requirements/
│   ├── architecture/
│   ├── diagrams/
│   ├── adr/
│   └── discovered/      (unmapped content from Phase 5)
├── documents/
│   ├── source/           (place source documents here)
│   ├── processed/         (converted markdown output)
│   └── templates/
├── scripts/
│   └── venv/              (created at runtime)
├── README.md
├── CHANGELOG.md
├── workflow.md
└── .gitignore
```

## Quick Start

1. **Clone the repository**
2. **Open in VSCode** with GitHub Copilot
3. **Copy the bootstrap prompt** from WORKFLOW.md into GitHub Copilot Chat
4. **Follow the 7-phase workflow**

## Workflow Phases

| Phase | Description |
|-------|-------------|
| 1 | File Structure Proposal |
| 2 | Source File Collection |
| 3 | Template Creation |
| 4 | Document Conversion |
| 5 | Content Mapping & Completeness Analysis |
| 6 | Documentation Update |
| 7 | Summary |

## Requirements

- Windows 11
- VSCode
- GitHub Copilot
- Python 3.11+

## Governance Rules

1. All paths must be relative to repository root
2. README.md must always exist and be kept current
3. CHANGELOG.md must be updated with structural/script changes
4. PowerShell commands only (no bash)
5. Never create files outside repository root

## License

MIT
