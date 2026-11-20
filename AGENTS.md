# Repository guide

- This is a collection of independent weekly exercises, not one Python workspace. Run `uv` commands from the exercise directory containing its `pyproject.toml`; there is no root-level test or lint command.
- Use Python 3.14 (`.python-version`); project manifests require `>=3.14`.

## Projects and checks

- `viikko1/nhl-statistics` and `viikko1/riippuvuuksien-injektointi`: run all tests with `uv run pytest`; target one test file with, for example, `uv run pytest src/tests/player_test.py` or `uv run pytest src/tests/laskin_test.py`.
- `viikko2/nhl-reader`: CLI entrypoint is `src/index.py` (`uv run python src/index.py`); tests are in `src/tests/` (`uv run pytest`); lint with `uv run pylint src`. Its `.pylintrc` excludes tests and sets unusually strict limits: `max-statements=10`, `max-args=4`, `max-nested-blocks=2`.
- `viikko2/uv-web`: `uv run uv-web` calls `main` in `src/uv_web/__init__.py`; currently it only prints a greeting, despite the FastAPI and SQLAlchemy dependencies.
- `viikko3/hello-robot`: run `uv run robot src/tests`; focus a suite with `uv run robot src/tests/increase_counter.robot`.
- `viikko4/maksukortti-mock` and `viikko4/verkkokauppa`: run `uv run pytest`; focused examples are `uv run pytest src/tests/kassapaate_test.py` and `uv run pytest src/tests/kauppa_test.py`, respectively.
- `viikko4/mock-demo`: run `uv run pytest`; unlike the other pytest exercises, modules and `index.py` are at the project root and tests are in `tests/` (`uv run pytest tests/kauppa_test.py`).

## Login browser tests (`viikko3/login`)

- Start the Flask app in a separate terminal with `uv run flask --app src/app run --host 127.0.0.1 --port 5000`, then run `uv run robot --variable HEADLESS:true src/tests` (or select a suite such as `src/tests/register.robot`). Tests default to visible Chromium without the `HEADLESS` override.
- `src/index.py` starts port **5001**, but both `src/tests/resource.robot` and `src/AppLibrary.py` target **5000**. Overriding Robot's `SERVER` alone does not redirect the Python helper.
- Routes and the Flask app are in `src/app.py`; credential validation is in `src/services/user_service.py`. Test setup resets application state via `POST /tests/reset` and creates users through HTTP using `AppLibrary.py`.
