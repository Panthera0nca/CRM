# CRM

CRM construido con Django. Gestiona contactos, empresas, negocios y actividades desde una interfaz limpia con Bootstrap 5.

## Funcionalidades

- **Dashboard** con métricas clave (contactos, empresas, negocios abiertos, valor ganado)
- **Contactos** — CRUD completo con historial de negocios y actividades
- **Empresas** — CRUD con listado de contactos asociados
- **Negocios** — pipeline en vista lista y vista Kanban por etapas (Lead → Ganado/Perdido)
- **Actividades** — registro de llamadas, emails, reuniones y notas

## Stack

- Python 3.12 / Django 5.0
- SQLite (desarrollo) / PostgreSQL-ready (producción)
- Bootstrap 5 vía CDN
- Whitenoise para archivos estáticos
- GitHub Actions para CI

## Instalación local

```bash
git clone https://github.com/Panthera0nca/CRM.git
cd CRM
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre http://localhost:8000
