# Repository guide

- This repository contains independent weekly exercises, not one Python workspace. Run `uv` commands from the relevant project directory; each project has its own `pyproject.toml` and `uv.lock`.
- Projects require Python 3.14 (`.python-version` / `requires-python`).

## Projects and checks

- `viikko1/nhl-statistics`: NHL statistics library/CLI; tests are in `src/tests/`. From this directory run `uv run pytest` (or a focused test, e.g. `uv run pytest src/tests/player_test.py`).
- `viikko1/riippuvuuksien-injektointi`: calculator exercise; tests are in `src/tests/`. From this directory run `uv run pytest` (or `uv run pytest src/tests/laskin_test.py`).
- `viikko2/nhl-reader`: CLI starts at `src/index.py`; it fetches season data from the Helsinki studies NHL stats endpoint. Run with `uv run python src/index.py`; lint with `uv run pylint src` (configured by `.pylintrc`). No tests are currently present.
- `viikko2/uv-web`: package entrypoint is `uv_web:main` in `src/uv_web/__init__.py`; no tests are currently present.

There is no root-level test or lint command; run checks separately in each project that has them.
