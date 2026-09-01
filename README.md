# ml-template

![CI](https://github.com/Brakselk/ml-template/actions/workflows/ci.yml/badge.svg)

Base template for ML projects: dependency management, linting, type
checking, tests, and a reproducible Docker build, wired into CI. Fork this
repo for each new project instead of starting from a blank notebook.

## Stack

- [uv](https://docs.astral.sh/uv/) for dependency management
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [mypy](https://mypy-lang.org/) (strict) for type checking
- [pytest](https://docs.pytest.org/) for tests
- [pre-commit](https://pre-commit.com/) to run the above before every commit
- Multi-stage `Dockerfile` for a slim runtime image
- GitHub Actions: lint → test → build

## Setup

```powershell
uv sync --all-groups
uv run pre-commit install
```

## Usage

```powershell
uv run pytest
uv run ruff check .
uv run mypy src
docker build -t ml-template .
```

## Layout

- `src/ml_template/seed.py` — deterministic seeding (random, numpy, torch)
- `src/ml_template/config.py` — YAML + env-based settings (pydantic-settings)
- `src/ml_template/repro.py` — captures the current git commit hash for run logging
- `configs/example.yaml` — example run config
