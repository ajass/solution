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
