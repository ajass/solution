# Solution Architect Workflow

## Table of Contents

1. [Overview](#overview)
2. [Governance Rules](#governance-rules)
3. [Folder Structure](#folder-structure)
4. [PowerShell Commands](#powershell-commands)
5. [Template Files](#template-files)
6. [Copilot Bootstrap Prompt](#copilot-bootstrap-prompt)
7. [Content Mapping Strategy](#content-mapping-strategy)
8. [Completeness Analysis](#completeness-analysis)
9. [Git Workflow & Versioning](#git-workflow--versioning)
10. [Artifact Lifecycle](#artifact-lifecycle)
11. [Naming Conventions](#naming-conventions)
12. [Diagram Standards](#diagram-standards)
13. [ADR Governance](#adr-governance)
14. [Change Management](#change-management)
15. [Automation Roadmap](#automation-roadmap)

---

## Overview

This workflow defines the process for a Solution Architect to:
- Establish a professional project folder structure
- Create and manage architecture artifacts
- Convert documents to Markdown using a Python virtual environment
- Populate standardized templates with converted content
- Analyze template completeness and identify gaps
- Maintain governance through README and CHANGELOG discipline

**Target Environment:** Windows 11, VSCode, GitHub Copilot, Python 3.11+, Local virtual environment (venv)

---

## Governance Rules

1. **Repository Boundary**: The project MUST NEVER create, reference, or assume directories outside the current repository root.
2. **Relative Paths Only**: All scripts must use relative paths from the repository root.
3. **Documentation Requirement**: A `README.md` must always exist and be kept current.
4. **Changelog Discipline**: A running `CHANGELOG.md` must be updated with every structural, script, or artifact change.
5. **Path Discipline**: All paths must be relative. All instructions assume execution from the repository root.
6. **PowerShell Only**: Use PowerShell commands, NOT bash.

---

## Folder Structure

```
/
├── artifacts/
│   ├── requirements/
│   ├── architecture/
│   ├── diagrams/
│   └── adr/
├── documents/
│   ├── source/
│   ├── processed/
│   └── templates/
├── scripts/
│   └── venv/          (created at runtime)
├── README.md
├── CHANGELOG.md
├── workflow.md
└── .gitignore
```

---

## PowerShell Commands

All scripts run without administrator privileges from the repository root. Virtual environment is located in `/scripts/venv`.

### Create Virtual Environment

```powershell
cd scripts
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
.\venv\Scripts\pip.exe install markitdown
```

### Run Document Converter

```powershell
.\venv\Scripts\python.exe convert_artifacts.py
```

### Deactivate Virtual Environment

```powershell
deactivate
```

**Note:** The `scripts/convert_artifacts.py` script is generated dynamically by Copilot during Phase 4 of the workflow. The script will:
- Use pathlib for relative paths
- Auto-install markitdown if not present
- Walk `/documents/source` recursively
- Preserve folder structure in `/documents/processed`
- Generate `error_log.md` for any conversion failures

---

## Template Files

All templates use Markdown with YAML frontmatter.

### Requirements Templates

**`templates/business-context.md`**
```yaml
---
title: Business Context
version: 0.1.0
author: 
date: 
status: draft
---
# Business Context

## Business Goals
-

## Business Scope
-

## Constraints
-

## Assumptions
-
```

**`templates/stakeholder-needs.md`**
```yaml
---
title: Stakeholder Needs
version: 0.1.0
author: 
date: 
status: draft
---
# Stakeholder Needs

## Stakeholder 1
- **Name:**
- **Role:**
- **Needs:**
-

## Stakeholder 2
- **Name:**
- **Role:**
- **Needs:**
-
```

**`templates/functional-requirements.md`**
```yaml
---
title: Functional Requirements
version: 0.1.0
author: 
date: 
status: draft
---
# Functional Requirements

## Requirement 1
- **ID:** FR-001
- **Description:**
- **Priority:**
- **Source:**
```

**`templates/non-functional-requirements.md`**
```yaml
---
title: Non-Functional Requirements
version: 0.1.0
author: 
date: 
status: draft
---
# Non-Functional Requirements

## Performance
-

## Security
-

## Scalability
-

## Availability
-

## Compliance
-
```

**`templates/traceability-matrix.md`**
```yaml
---
title: Traceability Matrix
version: 0.1.0
author: 
date: 
status: draft
---
# Traceability Matrix

| Requirement ID | Requirement | Stakeholder | Priority | Status |
|---------------|-------------|-------------|----------|--------|
| FR-001        |             |             |          |        |
```

### Architecture Templates

**`templates/current-state.md`**
```yaml
---
title: Current State Architecture
version: 0.1.0
author: 
date: 
status: draft
---
# Current State Architecture

## Systems
-

## Integrations
-

## Pain Points
-

## Technical Debt
-
```

**`templates/future-state.md`**
```yaml
---
title: Future State Architecture
version: 0.1.0
author: 
date: 
status: draft
---
# Future State Architecture

## Vision
-

## Target Systems
-

## Target Integrations
-

## Key Architectural Decisions
-
```

**`templates/gap-analysis.md`**
```yaml
---
title: Gap Analysis
version: 0.1.0
author: 
date: 
status: draft
---
# Gap Analysis

## Gap 1
- **Description:**
- **Impact:**
- **Priority:**
- **Mitigation:**
```

**`templates/roadmap.md`**
```yaml
---
title: Implementation Roadmap
version: 0.1.0
author: 
date: 
status: draft
---
# Implementation Roadmap

## Phase 1
- **Timeline:**
- **Deliverables:**
-

## Phase 2
- **Timeline:**
- **Deliverables:**
-
```

### Diagram Templates

**`templates/context-diagram.md`**
```yaml
---
title: C4 Context Diagram
version: 0.1.0
author: 
date: 
status: draft
diagram_type: c4_context
---
# C4 Context Diagram

```mermaid
C4Context
    Person(personalias, "Label", "Technology")
    System(systemalias, "Label", "Technology")
    SystemDb(dbalias, "Label", "Technology")
    Rel(personalias, systemalias, "Uses")
    Rel(systemalias, dbalias, "Stores data in")
```
```

**`templates/container-diagram.md`**
```yaml
---
title: C4 Container Diagram
version: 0.1.0
author: 
date: 
status: draft
diagram_type: c4_container
---
# C4 Container Diagram

```mermaid
C4Container
    Container(container_alias, "Container Name", "Technology", "Description")
    System_Ext(ext, "External System", "Description")
    Rel(container_alias, ext, "Uses")
```
```

**`templates/component-diagram.md`**
```yaml
---
title: C4 Component Diagram
version: 0.1.0
author: 
date: 
status: draft
diagram_type: c4_component
---
# C4 Component Diagram

```mermaid
C4Component
    ContainerDb(db, "Database", "Technology", "Description")
    Component(comp, "Component", "Technology", "Description")
    Rel(comp, db, "Reads/Writes")
```
```

**`templates/code-diagram.md`**
```yaml
---
title: Code Diagram
version: 0.1.0
author: 
date: 
status: draft
diagram_type: sequence|class|state
---
# Code Diagram

```mermaid
sequenceDiagram
    A->>B: Message
    B-->>A: Response
```
```

### ADR Template

**`templates/adr-template.md`**
```yaml
---
title: Architecture Decision Record
adr_id: 
date: 
status: proposed|accepted|deprecated|superseded
---
# ADR-: Title

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Status
proposed | accepted | deprecated | superseded

## Consequences
What becomes easier or more difficult to do because of this change?

### Positive
-

### Negative
-

### Neutral
-

## Related ADRs
-
```

---

## Copilot Bootstrap Prompt

Copy and paste the following into GitHub Copilot Chat to initiate the workflow:

---

```
You are a Solution Architect workflow assistant. Execute the following workflow phases sequentially, waiting for user confirmation before proceeding to each phase.

## PHASE 1: FILE STRUCTURE PROPOSAL
Review the required folder structure:
/
├── artifacts/
│   ├── requirements/
│   ├── architecture/
│   ├── diagrams/
│   └── adr/
├── documents/
│   ├── source/
│   ├── processed/
│   └── templates/
├── scripts/
├── README.md
├── CHANGELOG.md
├── workflow.md
└── .gitignore

Propose this structure to the user. Ask: "Does this file structure work for your project? Should I proceed with scaffolding?"

## PHASE 2: SOURCE FILE COLLECTION
After Phase 1 approval, inform the user:
"Place all source documents (meeting notes, transcripts, screenshots, pptx, docx, excel, pdf, etc.) in /documents/source. When ready, confirm by saying 'I'm ready to convert' and I will proceed."

Wait for the user to confirm they have placed files and are ready.

## PHASE 3: TEMPLATE CREATION
After Phase 2 confirmation, copy all template files from /documents/templates to their respective artifact directories:
- documents/templates/requirements/*.md -> artifacts/requirements/
- documents/templates/architecture/*.md -> artifacts/architecture/
- documents/templates/diagrams/*.md -> artifacts/diagrams/
- documents/templates/adr/*.md -> artifacts/adr/

Show the user the populated templates and ask: "Should I proceed with document conversion?"

## PHASE 4: DOCUMENT CONVERSION
After Phase 3 approval:
1. Generate the Python conversion script `scripts/convert_artifacts.py` with these requirements:
   - Use pathlib for relative paths from repo root
   - Create virtual environment in /scripts/venv
   - Auto-install markitdown if not present
   - Walk /documents/source recursively
   - Preserve folder structure in /documents/processed
   - Convert all supported formats (docx, pptx, xlsx, pdf, images, markdown)
   - Generate error_log.md for any failures
   - Run without admin privileges
2. Show the generated script to the user for approval
3. Create and activate the virtual environment:
   cd scripts
   python -m venv venv
   .\venv\Scripts\Activate.ps1
4. Install dependencies:
   .\venv\Scripts\pip.exe install markitdown
5. Run the converter:
   .\venv\Scripts\python.exe convert_artifacts.py
6. Display the results showing converted files and any errors
7. If errors exist, show the error log and ask: "Some files failed to convert. Should I continue with mapping or address the errors first?"

## PHASE 5: CONTENT MAPPING & COMPLETENESS ANALYSIS
After Phase 4 completion:
1. Read each converted document from /documents/processed/
2. Analyze filenames to determine content mapping:
   - meeting*, transcript*, notes* -> stakeholder-needs.md
   - requirements*, specs* -> functional-requirements.md
   - nfr*, non-functional* -> non-functional-requirements.md
   - decision*, adr* -> adr/adr-template.md (rename appropriately)
   - screenshot*, image* -> diagrams/
   - current*, existing* -> current-state.md
   - future*, target* -> future-state.md
   - roadmap*, timeline* -> roadmap.md
   - gap* -> gap-analysis.md
3. Populate the appropriate templates with extracted content
4. Generate a completeness-report.md in /artifacts/architecture/ analyzing:
   - Which templates have content
   - Which templates are empty or missing sections
   - Suggested next steps to complete the portfolio
5. Display the completeness report to the user
6. Ask: "I have analyzed template completeness. The report shows [summary]. Would you like to add more source files to address gaps? Say 'yes' to add more files or 'no' to proceed."

## PHASE 5 LOOP
If user says "yes":
- Ask user to add files to /documents/source
- Wait for confirmation "I'm ready"
- Re-run conversion (Phase 4)
- Re-run completeness analysis (Phase 5)
If user says "no":
- Proceed to Phase 6

## PHASE 6: DOCUMENTATION UPDATE
After Phase 5 completion:
1. Update README.md with:
   - Project purpose and description
   - Folder structure explanation
   - Setup instructions
   - Script usage
   - Governance rules
   - Current artifact status
2. Update CHANGELOG.md:
   - Add entry under "Unreleased" or appropriate version
   - Document: new templates, converted documents, structural changes
3. Show the user the proposed updates and ask: "Should I commit these documentation changes?"

## PHASE 7: SUMMARY
After Phase 6 approval:
1. Summarize what was accomplished:
   - Files converted
   - Templates populated
   - Completeness status
   - Next recommended steps
2. Provide guidance on:
   - How to view rendered Mermaid diagrams
   - How to manually complete remaining templates
   - How to add more artifacts later

## GUARDRAILS
- NEVER create files outside the repository root
- ALWAYS use PowerShell commands, not bash
- ALWAYS wait for user confirmation before proceeding to the next phase
- If ANY error occurs, report it clearly and ask for guidance
- NEVER overwrite existing user content without confirmation
```

---

## Content Mapping Strategy

### Filename-Based Heuristics

| Filename Pattern | Target Template |
|-----------------|-----------------|
| `meeting*`, `transcript*`, `notes*` | `artifacts/requirements/stakeholder-needs.md` |
| `requirement*`, `spec*`, `feature*` | `artifacts/requirements/functional-requirements.md` |
| `nfr*`, `non-functional*`, `performance*`, `security*` | `artifacts/requirements/non-functional-requirements.md` |
| `decision*`, `adr*` | `artifacts/adr/<descriptive-name>.md` |
| `screenshot*`, `image*`, `diagram*` | `artifacts/diagrams/` |
| `current*`, `existing*`, `as-is*` | `artifacts/architecture/current-state.md` |
| `future*`, `target*`, `to-be*` | `artifacts/architecture/future-state.md` |
| `roadmap*`, `timeline*`, `plan*` | `artifacts/architecture/roadmap.md` |
| `gap*`, `analysis*` | `artifacts/architecture/gap-analysis.md` |
| `context*`, `overview*` | `artifacts/requirements/business-context.md` |
| `trace*`, `matrix*` | `artifacts/requirements/traceability-matrix.md` |

### Mapping Priority

1. Exact matches take priority (case-insensitive)
2. Partial matches are considered secondary
3. Unmatched files remain in `/documents/processed/` for manual review

---

## Completeness Analysis

### Generated Report: `completeness-report.md`

After mapping content, generate `/artifacts/architecture/completeness-report.md`:

```yaml
---
title: Template Completeness Report
version: 0.1.0
generated: 
status: draft
---
# Template Completeness Report

## Summary
- **Total Templates:** X
- **Populated:** X
- **Empty/Incomplete:** X
- **Completion Rate:** X%

## Template Status

| Template | Status | Content Found | Next Steps |
|----------|--------|---------------|------------|
| business-context.md | Complete/Empty/Partial | | |
| stakeholder-needs.md | Complete/Empty/Partial | | |
| functional-requirements.md | Complete/Empty/Partial | | |
| non-functional-requirements.md | Complete/Empty/Partial | | |
| traceability-matrix.md | Complete/Empty/Partial | | |
| current-state.md | Complete/Empty/Partial | | |
| future-state.md | Complete/Empty/Partial | | |
| gap-analysis.md | Complete/Empty/Partial | | |
| roadmap.md | Complete/Empty/Partial | | |
| context-diagram.md | Complete/Empty/Partial | | |
| container-diagram.md | Complete/Empty/Partial | | |
| component-diagram.md | Complete/Empty/Partial | | |
| adr/*.md | Complete/Empty/Partial | | |

## Recommendations

### High Priority
-

### Medium Priority
-

### Low Priority
-

## Action Items
-
```

### Completeness Criteria

| Template | Complete If |
|----------|-------------|
| `business-context.md` | Business goals, scope, constraints all present |
| `stakeholder-needs.md` | At least 3 stakeholders with needs defined |
| `functional-requirements.md` | At least 5 requirements with IDs |
| `non-functional-requirements.md` | Performance, security, scalability defined |
| `traceability-matrix.md` | At least one linked requirement |
| `current-state.md` | Systems, integrations, pain points documented |
| `future-state.md` | Vision and target architecture described |
| `gap-analysis.md` | At least 1 gap identified |
| `roadmap.md` | At least 1 phase defined |
| Diagram templates | Mermaid code block present |
| ADR templates | Context, Decision, Status, Consequences all filled |

---

## Git Workflow & Versioning

### Branching Model

```
main
├── feature/
│   ├── requirements/
│   ├── architecture/
│   └── diagrams/
├── docs/
│   ├── templates/
│   └── templates/
```

### Version Bump Triggers

| Version Change | Trigger |
|---------------|---------|
| v0.1.0 | Initial project setup |
| v0.2.0 | New templates added or structural changes |
| v0.3.0 | Significant content added to templates |
| v1.0.0 | First "production" deliverable - portfolio complete |

### Commit Message Convention

```
<type>(<scope>): <description>

[optional body]

Types: feat, docs, template, script, refactor
```

---

## Artifact Lifecycle

| Phase | Description | Status |
|-------|-------------|--------|
| **Draft** | Initial creation, incomplete | `draft` |
| **Review** | Under stakeholder review | `review` |
| **Approved** | Reviewed and approved | `approved` |
| **Deprecated** | Superseded by newer version | `deprecated` |

### Lifecycle Rules

1. All artifacts start as `draft`
2. Artifacts require approval before marking as `approved`
3. Deprecated artifacts must link to superseding artifact
4. Version increments on status change from `draft` to `approved`

---

## Naming Conventions

### Files
- Use kebab-case: `functional-requirements.md`
- Use descriptive names: `adr-001-database-choice.md`

### Folders
- Use kebab-case: `artifacts/requirements/`
- Group related: `adr/` for all ADRs

### Diagrams
- Include type prefix: `c4-context-overview`, `c4-container-system`
- Use `.md` extension with embedded Mermaid

---

## Diagram Standards

### Engine
- **Mermaid.js** - Native GitHub/GitLab markdown rendering

### C4 Model Levels
1. **Context** - External actors and systems
2. **Container** - Applications and data stores
3. **Component** - Internal components within containers
4. **Code** - Class diagrams, sequence diagrams

### Diagram Checklist
- [ ] All diagrams use Mermaid code blocks
- [ ] Labels are descriptive
- [ ] Relationships are clearly defined
- [ ] Diagram type is documented in YAML frontmatter

---

## ADR Governance

### ADR Numbering
- Sequential: ADR-001, ADR-002, etc.
- Format: `artifacts/adr/adr-XXX-title.md`

### ADR Status Flow
```
proposed → accepted
      ↘         ↙
    rejected  deprecated → superseded
```

### Required Sections
1. Context (problem statement)
2. Decision (the choice made)
3. Status (current state)
4. Consequences (positive, negative, neutral)
5. Related ADRs (links)

---

## Change Management

### Change Request Process

1. **Identify** - Document what needs to change
2. **Assess** - Evaluate impact on existing artifacts
3. **Propose** - Create new draft or modify existing
4. **Review** - Stakeholder review
5. **Approve** - Status change to `approved`
6. **Document** - Update CHANGELOG.md

### Documentation Triggers

Update CHANGELOG.md when:
- New template created
- Existing template significantly modified
- New artifacts added
- Folder structure changes
- Script changes

---

## Automation Roadmap

### Phase 1 (Current)
- Manual document conversion via script
- Manual template population
- Manual completeness analysis

### Phase 2 (Future)
- Automated filename pattern detection
- Content extraction heuristics
- Template auto-population

### Phase 3 (Future)
- AI-assisted content summarization
- Automatic diagram generation from descriptions
- Completeness scoring with recommendations

### Phase 4 (Future)
- Full workflow automation
- Template validation rules
- Integrated stakeholder review workflow
