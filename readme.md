# Flask App with Docker

A simple Python Flask application that:

- Displays a message on the home page from the environment variable `APP_MESSAGE`.
- Shows the app health on `/health` from the environment variable `APP_HEALTH`.
- Uses Docker and GitHub Actions for containerization and automated builds.
- Dependabot is configured for weekly dependency updates.
