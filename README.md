# Django Project with Docker Compose

This README provides instructions for setting up and running the Django project using Docker Compose.  This setup utilizes separate containers for the Django application, PostgreSQL database, Redis, and Celery.

## Prerequisites

*   [Docker](https://www.docker.com/)
*   [Docker Compose](https://docs.docker.com/compose/)
*   A `.env` file in the project root containing the necessary environment variables (see `.env.example`).  **Crucially, ensure your `DATABASE_PASSWORD`, `SECRET_KEY`,  `STRIPE_TEST_SECRET_KEY`, and `STRIPE_TEST_PUBLIC_KEY` are appropriately set and secure.**


## Setup

1.  **Clone the repository:**
    git clone <your_repository_url>
    cd <your_repository_name>
    ```

2.  **Create the `.env` file:** Copy the `.env.template` file to `.env` and fill in the required environment variables.  Use a secure method for managing sensitive information like database passwords.

3.  **Create the `media` directory:**  Create an empty `media` directory at the root of your project. This will store uploaded files.

4.  **Build the Docker images and start the containers:**
    docker-compose up -d --build
    ```
    This command builds the Docker images (if necessary) and starts the containers in detached mode (running in the background).

## Accessing the Application

Once the containers are running, you can access your Django application through your web browser at `http://localhost:8000`.

## Migrations and Database Setup

After starting the containers, you need to run Django migrations:

docker-compose exec web python manage.py migrate

You can then run any other necessary management commands such as creating a superuser:

docker-compose exec web python manage.py createsuperuser

Stopping the Containers

To stop the containers, run:

docker-compose down

Useful Commands

    docker-compose up -d --build: Starts all services in detached mode (background).
    docker-compose down: Stops all services.
    docker-compose logs: Displays logs from all services.
    docker-compose exec web python manage.py <command>: Runs a Django management command within the web container (replace <command> with the desired command).

Troubleshooting

    Ensure all ports (specified in docker-compose.yml) are not already in use on your system.
    Check the logs for errors using docker-compose logs.
    Verify that your environment variables are correctly set in the .env file.
    
Remember to replace `<your_repository_url>` and `<your_repository_name>` with your actual repository URL and name.  This README provides a clear and concise guide for users to set up and run your project.  The inclusion of troubleshooting tips improves the user experience.