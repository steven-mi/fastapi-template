# FastAPI Template

FastAPI template to easily bootstrap a project. The template contains:

- Simple FastAPI Application
- Poetry for Dependency Management
- GitHub Action for CI
- Ruff as Python Linter
- Devcontainer for development environment

## Getting Started

### Start FastAPI Application

```
uvicorn src.main:app  --reload 
```

### Format Files

```
black .
```

### Linter

```
ruff check
```

## TODOs
- Add alembic + Postgres + SQLAlchemy boilerplate
- Add CRUD boilerplate
