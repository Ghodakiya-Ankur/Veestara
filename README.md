# Sports Daily

Welcome to Sports Daily, your go-to source for the latest sports news and updates. Sports Daily is a dynamic web application built using Python Django, offering a comprehensive platform for sports enthusiasts to stay informed about their favorite teams, athletes, and events.

## Requirements

To get started with Sports Daily, ensure the following dependencies are installed on your system:

- Python (version 3.6 or higher)
- Django
- PostgreSQL

## Installation

1. Make sure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install Django using pip:

pip install django


3. Install PostgreSQL and create a new database for Sports Daily. Download PostgreSQL from [here](https://www.postgresql.org/download/) and follow the installation instructions.

## Setting Up the Project

1. Download the Sports Daily source code folder to your local machine.

2. Navigate to the project directory in your terminal or command prompt.

3. Create a virtual environment (optional but recommended):

python -m venv env


4. Activate the virtual environment:

   On Windows:


env\Scripts\activate


6. Configure the database settings:
- Open `settings.py` located in the `SportsDaily` directory.
- Update the `DATABASES` dictionary with your PostgreSQL settings.

## Running the Project

1. Apply migrations to create database tables:

python manage.py migrate


2. Start the Django development server:

python manage.py runserver


3. Access Sports Daily in your web browser at `http://127.0.0.1:8000/`.

## Usage

- As a User:
  - Browse through the latest sports news, articles, and updates.
  - Search for specific teams, players, or events.
  - Interact with the community through comments and discussions.

- As an Admin:
  - Manage user accounts and permissions.
  - Create, edit, and delete articles and news posts.
  - Monitor user interactions and maintain the integrity of the platform.

Thank you for choosing Sports Daily! We hope you enjoy staying up-to-date with the exciting world of sports!
