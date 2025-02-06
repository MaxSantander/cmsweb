
# Web Backend

RIS-Web Backend is a custom Content Management System (CMS) built on Django. It is designed for high-performance, multilingual web content management using a dynamic page block system, Redis caching, and a robust PostgreSQL backend.

## Features

- **Multilingual Content Management:** Supports German and English content with language-specific URL routing.
- **High-Performance Caching:** Uses Redis for template caching and session management.
- **RESTful API:** Provides full CRUD functionality for pages, blocks, and menu items.
- **Dynamic Page Block System:** Flexible assignment and ordering of reusable content blocks.
- **Normalized Database Design:** Implemented with PostgreSQL ensuring optimized schema (1NF, 2NF, 3NF).
- **Versioning:** Integrated with Django Simple History for change tracking.
- **Agile Development:** Maintained through continuous integration (GitLab CI) and modern development practices.

## Project Structure

```
ris_dev/
├── _doc/                  # Documentation source and build files (Sphinx)
├── build/                 # Build outputs
├── documentation/         # Additional documentation scripts and assets
├── 

manage.py

              # Django management entry point
├── pages_app/             # Core application with models, views, and templates
├── ris_prj/               # Project settings and configurations
├── templates/             # Django template files
├── tools/                 # Utility scripts
├── venv/                  # Virtual environment
├── ...                    # Other supporting files (Makefile, .env, etc.)
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/risdev.git
   cd risdev
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**  
   Create a 

.env

 file at the project root with the following (adjust as necessary):
   ```
   DJANGO_SETTINGS_MODULE=ris_prj.settings.development
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
   REDIS_URL=redis://127.0.0.1:6379/1
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=your_email_password
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Documentation

Comprehensive project documentation (including API references and technical details) is maintained using Sphinx. To build the HTML documentation:
```bash
cd _doc
make html
```
The generated documentation will be available in 

html

.

## Technologies

- **Backend Framework:** Django
- **Language:** Python 3.8+
- **Database:** PostgreSQL (normalized to 3NF)
- **Caching:** Redis
- **API:** RESTful endpoints
- **Versioning:** Django Simple History
- **Web Server & Deployment:** Gunicorn, Nginx, WhiteNoise
- **CI/CD:** GitLab CI

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

For further information, please contact:

- **Max Santander**  
  Email: max.santander@outlook.com  
  Location: Regensburg, Germany
```
