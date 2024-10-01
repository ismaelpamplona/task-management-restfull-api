# Task Management RESTful API

🐍 A RESTful API for a Task Management app built with Python, Flask, and MongoDB. Manage projects, tasks, and subtasks with features like authentication, caching, pagination, and more! Follows OOP principles, SOLID, and best practices. Designed to be fast, scalable, and developer-friendly!

## 🚀 Features

## 📚 Technologies Used

## 📋 Improvements

## 📑 Issue Management

This application uses [ripissue](https://github.com/cwnt-io/ripissue) to manage issues with Git and the filesystem.

## 🐳 Running the Application with Docker

### 🔧 Configuration

The application reads environment variables from the dev.env file. Make sure to create one with the following keys:

```bash
# Flask Environment
FLASK_ENV=development
MONGO_URI=mongodb://root:example@mongo:27017/task_management?authSource=admin

# MongoDB
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example

# Mongo Express Configuration
ME_CONFIG_MONGODB_ADMINUSERNAME=root
ME_CONFIG_MONGODB_ADMINPASSWORD=example
ME_CONFIG_MONGODB_URL=mongodb://root:example@mongo:27017/admin
ME_CONFIG_BASICAUTH=false

# JWT
JWT_SECRET_KEY=supersecretkey123
```

### 🚀 Start application

Ensure you have Docker and Docker Compose installed on your machine. You can start the application with:

```bash
docker compose up --build
```

### Database Setup

After starting the containers, you need to perform the following steps to set up the database:

#### Run Migrations

```bash

```

#### Apply Seed Data (Optional)

```bash

```

### 🧪 Testing the Application with Docker

The application follows a **Test-Driven Development (TDD)** paradigm. All features are thoroughly tested using `pytest`, ensuring that each functionality works as expected. To run the tests, execute:

```bash
docker compose exec flask-app poetry run pytest -s
```

## Access Swagger Documentation

```bash

```

## 💡 Contributing

Contributions are welcome! Please feel free to submit a Pull Request for any enhancements, bug fixes, or documentation improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
