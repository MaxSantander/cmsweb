Deployment
==========

Overview
--------
This section provides guidelines for deploying the RIS-Web Backend to a production environment.

Deployment Steps
----------------
1. Set up the production environment:
   - Install necessary software (e.g., PostgreSQL, Redis, Nginx)
   - Configure environment variables

2. Collect static files:
   .. code-block:: bash

      python manage.py collectstatic

3. Apply database migrations:
   .. code-block:: bash

      python manage.py migrate

4. Configure Gunicorn:
   - Create a Gunicorn service file
   - Start the Gunicorn service

5. Configure Nginx:
   - Set up Nginx to serve static files and proxy requests to Gunicorn

6. Enable HTTPS:
   - Obtain an SSL certificate (e.g., Let's Encrypt)
   - Configure Nginx for HTTPS

Example Configuration
---------------------
Example Gunicorn service file:
.. code-block:: ini

   [Unit]
   Description=gunicorn daemon
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/your/project
   ExecStart=/path/to/your/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/your/project.sock ris_prj.wsgi:application

   [Install]
   WantedBy=multi-user.target

Example Nginx configuration:
.. code-block:: nginx

   server {
       listen 80;
       server_name your-domain.com;

       location /static/ {
           alias /path/to/your/project/static/;
       }

       location / {
           proxy_pass http://unix:/path/to/your/project.sock;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
