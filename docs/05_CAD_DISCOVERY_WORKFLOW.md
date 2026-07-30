# CAD Discovery Workflow

Before generating a new CAD model MyEngineer must search existing solutions.

Pipeline:

```
Engineering Request
        ↓
CAD Discovery Agent
        ↓
Search Existing Models
        ↓
Similarity Analysis
        ↓
Reuse / Modify / Create New
```

Search targets:

- STEP libraries
- STL repositories
- manufacturer CAD portals
- open hardware projects
- GitHub repositories

Decision:

1. Existing model found → evaluate reuse.
2. Partial match → modify existing design.
3. No match → generate new CAD.
