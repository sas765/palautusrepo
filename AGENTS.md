# Repository guide

- This is a collection of independent weekly exercises, not one Python workspace. Run `uv` commands from the exercise directory containing its `pyproject.toml`; there is no root-level test or lint command.
- The Python projects require Python 3.14.

## Projects and checks

- `viikko1/nhl-statistics` and `viikko1/riippuvuuksien-injektointi`: run all tests with `uv run pytest`; target one test file with, for example, `uv run pytest src/tests/player_test.py` or `uv run pytest src/tests/laskin_test.py`.
- `viikko2/nhl-reader`: CLI entrypoint is `src/index.py` (`uv run python src/index.py`); tests are in `src/tests/` (`uv run pytest`); lint with `uv run pylint src` using `.pylintrc`.
- `viikko2/uv-web`: console entrypoint is `uv-web` (`uv run uv-web`), implemented by `src/uv_web/__init__.py`.
- `viikko3/hello-robot`: Robot Framework tests are in `src/tests/`; run with `uv run robot src/tests`.
- `viikko3/login`: Flask app entrypoint is `src/index.py`; browser tests are in `src/tests/` and run with `uv run robot src/tests`. The tests and their helper target `127.0.0.1:5000`, while `src/index.py` starts the app on port `5001`; start the app on the expected test port before running them. Username and password are validated in `src/services/user_service.py`.
