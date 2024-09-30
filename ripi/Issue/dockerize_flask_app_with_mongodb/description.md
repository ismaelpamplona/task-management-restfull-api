# dockerize_flask_app_with_mongodb (Issue)

- [x] Create a Dockerfile for the Flask app:

  - [x] Write a Dockerfile to containerize the Flask application.
  - [x] Build and test the Docker image for the Flask app.

- [x] Create a `compose.yml` file:

  - [x] Define the Flask service in `docker-compose.yml`.
  - [x] Define the MongoDB service in `docker-compose.yml`.

- [x] Test the setup:
  - [x] Start the services using `docker-compose`.
  - [x] Verify that the Flask app is running correctly and can connect to MongoDB.

```json
// 20240929224549
// http://localhost:5000/check-mongo

{
  "databases": ["admin", "config", "local"],
  "message": "Connected to MongoDB"
}
```
