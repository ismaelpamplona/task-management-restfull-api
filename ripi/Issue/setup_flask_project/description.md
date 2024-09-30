# setup_flask_project (Issue)

- [x] Initialize the project with Poetry:
  - [x] Create a `pyproject.toml` file using Poetry.
  - [x] Add Flask as a dependency.
  - [x] Add pytest as a development dependency.
- [ ] Create the initial Flask application structure:
  - [ ] Create the project directories (`app/`, `app/routes/`, `tests/`).
  - [ ] Implement a simple `create_app()` function in `app/__init__.py`.
  - [ ] Set up a basic route in `app/routes/index.py` to return a "Welcome" message.
- [ ] Write the first test for the welcome route:
  - [ ] Write a failing test to check that the route returns the expected "Welcome" message.
  - [ ] Make the test pass by running it using pytest.
- [x] Create a `.gitignore` file:
  - [x] Ensure it ignores all files that shouldn't be committed (e.g., `__pycache__/`, `.venv/`, `.pytest_cache/`).
