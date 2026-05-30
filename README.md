# Argon Dashboard Django

A Django-based admin dashboard built on top of the Argon Dashboard Bootstrap 4 UI kit.
The application provides session-based authentication (login, registration, logout) and a
set of pre-built UI pages including tables, maps, icons, and a user profile view. It is
structured as a modular Django project suitable for use as a starter template or as the
foundation for a data-driven internal tool.

---

## Architecture / Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.9 |
| Web framework | Django 3.2 LTS |
| UI kit | Argon Dashboard (Bootstrap 4) |
| Static files | WhiteNoise |
| Database | SQLite (default), configurable via `dj-database-url` |
| WSGI server | Gunicorn |
| Reverse proxy | Nginx (Docker deployment) |
| Containerisation | Docker / Docker Compose |
| Configuration | python-decouple (`.env` file) |

---

## Project Structure

```
argon-dashboard-django/
├── apps/
│   ├── authentication/         # Login, registration, logout
│   │   ├── config.py           # AppConfig
│   │   ├── forms.py            # LoginForm, SignUpForm
│   │   ├── urls.py             # /login, /register, /logout
│   │   └── views.py            # login_view, register_user
│   ├── home/                   # Authenticated dashboard pages
│   │   ├── config.py           # AppConfig
│   │   ├── urls.py             # / and catch-all *.html routes
│   │   └── views.py            # index, pages
│   ├── static/                 # CSS, JS, image assets
│   └── templates/
│       ├── accounts/           # login.html, register.html
│       ├── home/               # Dashboard pages (index, tables, maps, …)
│       ├── includes/           # Reusable partials (nav, sidebar, footer)
│       └── layouts/            # Base templates
├── core/
│   ├── settings/
│   │   ├── __init__.py         # Selects dev or production settings via DJANGO_ENV
│   │   ├── base.py             # Common settings
│   │   ├── development.py      # DEBUG=True
│   │   └── production.py      # Production hardening
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── nginx/
│   └── appseed-app.conf        # Nginx reverse proxy config
├── .env.example                # Environment variable template
├── docker-compose.yml
├── Dockerfile
├── gunicorn.conf.py
├── manage.py
├── pyproject.toml
├── requirements.txt
└── runtime.txt
```

---

## Local Setup and Installation

**Prerequisites:** Python 3.9+, pip

### 1. Clone the repository

```bash
git clone https://github.com/T0MYAMMM/argon-dashboard-django.git
cd argon-dashboard-django
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate        # Linux / macOS
# env\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env and set SECRET_KEY and any other values for your environment
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The application is available at `http://127.0.0.1:8000/`.

---

## Docker Deployment

```bash
# Build and start all services (Django app + Nginx)
docker-compose up --build -d

# The app is served at http://localhost:85
```

The `DJANGO_ENV=production` environment variable should be set in your `.env` file when
running in Docker to activate production-hardened settings.

---

## Usage

- Visit `http://127.0.0.1:8000/register/` to create an account.
- Log in at `http://127.0.0.1:8000/login/`.
- All dashboard routes under `/` require authentication and redirect to the login page otherwise.
- The Django admin panel is available at `http://127.0.0.1:8000/admin/`.

### CSS Recompilation (optional)

The UI assets use Sass. To recompile after making style changes:

```bash
cd apps/static/assets
npm install
npm install -g gulp-cli
gulp scss
```

---

## Future Improvements

- Upgrade to Django 4.x or 5.x and update all pinned dependencies accordingly.
- Replace SQLite with PostgreSQL for production deployments; the `dj-database-url`
  dependency is already included to support this via the `DATABASE_URL` environment variable.
- Add a comprehensive test suite using `pytest-django`, covering authentication flows and
  view responses.
- Introduce a `UserProfile` model to extend the built-in `User` with avatar and bio fields,
  enabling the profile page to display dynamic data.
- Add `django-debug-toolbar` to the development settings for query inspection.
- Configure a CI pipeline (GitHub Actions) to run linting and tests on every pull request.
