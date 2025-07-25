# AMKA Backend

Production-grade Django backend for the **AMKA Youth Movement**.  
**Modular, secure, API-first, Dockerized, and ready for scale.**

---

## 🚀 Features

- Custom User Model (with strict validation, region, phone required)
- Event Management (CRUD, API, filtering, featured)
- News & Announcements (rich text, publish/draft, SEO slugs)
- Gallery (image uploads, categories, tags, admin bulk actions)
- Dynamic Forms (registration/join, contributions, messages – with region logic)
- Notifications (email, SMS, in-app – Celery-ready, admin logs)
- Audit Log (every key action, admin/user, model change)
- Modern Admin Panel (Grappelli/Jet ready, custom filters & actions)
- JWT Authentication (secure login/logout endpoints for API)
- API-first (RESTful, paginated, filter/search, OpenAPI docs)
- Environment-driven (uses `.env` for secrets/config)
- Dockerized (Django + Postgres + Redis, out-of-the-box)
- S3/Cloudinary ready for media files
- Error monitoring, Sentry integration ready
- Caching, security best-practices, analytics hooks
- Scaffolded for pytest, CI/CD, and full test coverage

---

## 🏁 Quickstart (Local Dev via Docker)

```bash
# Clone this repo
git clone https://github.com/YOUR-ORG/amka-backend.git
cd amka-backend

# Create .env config (see sample below)
cp .env.example .env

# Build and start all services (Django + Postgres + Redis)
docker-compose up --build

# In a separate terminal, run migrations and create an admin user:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# Visit the app (default: http://localhost:8000)
# Admin panel: http://localhost:8000/admin/
⚙️ .env Example
env
Copy
Edit
SECRET_KEY=replace-this-with-a-strong-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DATABASE_URL=postgres://amka_admin:strongpassword@db:5432/amka
REDIS_URL=redis://redis:6379/0
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
SENTRY_DSN=
🧩 Project Structure
bash
Copy
Edit
amka-backend/
│
├── apps/
│   ├── users/           # Custom user model & auth
│   ├── events/          # Events management
│   ├── news/            # Announcements/news
│   ├── gallery/         # Media gallery
│   ├── forms/           # Dynamic forms (registration etc)
│   ├── notifications/   # Email/SMS/in-app notifications
│   ├── audit/           # Audit log
│   └── ...              # More apps as needed
│
├── amka_backend/        # Project config & settings
│   ├── settings/
│   ├── urls.py
│   └── ...
├── requirements/
│   └── base.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
📚 API Documentation
Swagger/OpenAPI: http://localhost:8000/api/docs/

Schema: http://localhost:8000/api/schema/

🔐 Authentication
JWT Auth endpoints (for frontend/mobile apps):

POST /api/token/ (obtain access/refresh token)

POST /api/token/refresh/ (refresh token)

POST /api/token/verify/ (verify token)

Admin Panel: /admin/ (session authentication)

🧪 Testing
bash
Copy
Edit
docker-compose exec web pytest
# or
docker-compose exec web python manage.py test
🚦 Deployment & Production Notes
Set DEBUG=False and configure ALLOWED_HOSTS for production!

Use AWS S3 or Cloudinary for media file storage.

Add your Sentry DSN for error monitoring.

Use SSL/TLS (via your hosting or a reverse proxy).

Use managed Postgres and Redis (on Railway, Render, DigitalOcean, AWS RDS, etc).

💡 Contributing
Pull requests and suggestions are welcome!
Open an issue to discuss new features, improvements, or bugs.

📝 License
MIT License
© AMKA Youth Movement

👥 Maintainers
[Your Name/Team] – [kailaevans254@gmail.com]