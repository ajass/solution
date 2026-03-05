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
