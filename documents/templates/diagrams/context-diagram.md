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
