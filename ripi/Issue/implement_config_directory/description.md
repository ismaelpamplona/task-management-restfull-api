# implement_config_directory (Issue)

- [x] Create a `config` directory:

  - [x] Create a `config.py` file inside the `config` directory.
  - [x] Implement a `Config` class to handle environment variables.

- [x] Load environment variables in `config.py`:

  - [x] Write a failing test to check that environment variables are loaded correctly.
  - [x] Use `python-dotenv` to load variables from `dev.env`.
  - [x] Make the test pass by validating that the Flask app reads the variables from the `Config` class.

- [ ] Integrate the `Config` class into the Flask app:

  - [ ] Update `create_app()` to use the `Config` class.
  - [ ] Write a test to ensure the configuration is applied correctly to the Flask app.
  - [ ] Make the test pass by validating the configuration integration.
