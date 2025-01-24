Getting Started
===============

Introduction
------------
Welcome to the RIS-Web Backend documentation. This section will guide you through the initial setup and configuration of the project.

Requirements
------------
* Python 3.8+
* PostgreSQL
* Redis
* Java (for PlantUML)

Installation Steps
------------------
Follow these steps to set up your development environment:

1. Clone the Repository
   ::

      git clone <repository-url>

2. Set Up Python Environment
   ::

      python -m venv .venv

      # On Windows
      .venv\Scripts\activate
      
      # On macOS/Linux
      source .venv/bin/activate

      pip install -r requirements.txt

Database Setup
--------------
1. Install and Configure PostgreSQL:

   .. code-block:: sql

      CREATE DATABASE ris_db;
      CREATE USER ris_admin WITH PASSWORD 'yourpassword';
      GRANT ALL PRIVILEGES ON DATABASE ris_db TO ris_admin;

2. Configure Environment
   Create a `.env` file with the following variables:

   .. code-block:: text

      DB_NAME=ris_db
      DB_USER=ris_admin
      DB_PASSWORD=yourpassword
      DB_HOST=localhost
      DB_PORT=5432
      REDIS_URL=redis://127.0.0.1:6379/1

3. Run Migrations
   ::

      python manage.py migrate

Start Development Server
----------------------------
Run the following command:
::

    python manage.py runserver

The application will be available at ``http://localhost:8000``.
