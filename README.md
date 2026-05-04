# CRM

Sistema de gestión de relaciones con clientes construido con Django. Permite gestionar contactos, empresas, negocios y actividades desde una interfaz limpia y responsiva.

---

## Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.12 / Django 5.0 |
| Base de datos | SQLite (desarrollo) · PostgreSQL (producción) |
| Frontend | Django Templates + Bootstrap 5 (CDN) + Bootstrap Icons |
| Archivos estáticos | Whitenoise |
| Servidor de producción | Gunicorn |
| CI/CD | GitHub Actions |

---

## Funcionalidades

- **Dashboard** — KPIs en tiempo real: total de contactos, empresas, negocios abiertos y valor acumulado ganado. Tabla de negocios y actividades recientes.
- **Contactos** — CRUD completo. Vista de detalle con negocios y actividades asociadas al contacto.
- **Empresas** — CRUD completo. Vista de detalle con todos los contactos de la empresa.
- **Negocios** — CRUD completo con dos vistas: lista y **Kanban** por etapas (Lead → Calificado → Propuesta → Ganado / Perdido).
- **Actividades** — Registro de llamadas, emails, reuniones y notas. Asociables a un negocio o contacto.
- **Admin** — Panel de administración Django con acceso completo a todas las entidades.

---

## Arquitectura

```
CRM/
├── apps/
│   ├── core/           # Dashboard y vista principal
│   ├── contacts/       # Módulo de contactos
│   ├── companies/      # Módulo de empresas
│   ├── deals/          # Módulo de negocios + Kanban
│   └── activities/     # Módulo de actividades
├── config/
│   ├── settings.py     # Configuración principal
│   ├── urls.py         # Enrutamiento raíz
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   ├── base.html       # Layout con sidebar y navbar
│   ├── core/
│   ├── contacts/
│   ├── companies/
│   ├── deals/
│   └── activities/
├── static/
├── manage.py
├── requirements.txt
└── .env.example
```

Cada app sigue el mismo patrón: `models.py` → `forms.py` → `views.py` (Class-Based Views) → `urls.py` → `templates/`.

---

## Variables de entorno

Copia `.env.example` a `.env` y ajusta los valores:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Para producción con PostgreSQL, agrega:

```env
DEBUG=False
ALLOWED_HOSTS=tudominio.com
DATABASE_URL=postgres://user:password@host:5432/dbname
```

---

## Instalación local

```bash
git clone https://github.com/Panthera0nca/CRM.git
cd CRM

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno
cp .env.example .env

# Crear tablas
python manage.py migrate

# Crear usuario administrador
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

Abre **http://localhost:8000**

Panel de administración: **http://localhost:8000/admin**

---

## Deploy

El proyecto está listo para deployar en plataformas como **Railway**, **Render** o **Fly.io**:

1. Configura las variables de entorno (`SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASE_URL`)
2. Instala `psycopg2-binary` para conectar PostgreSQL: `pip install psycopg2-binary`
3. Corre `python manage.py collectstatic` para compilar los estáticos
4. Usa Gunicorn como servidor: `gunicorn config.wsgi:application`

---

## CI

GitHub Actions corre automáticamente en cada push a `main`:
- Instala dependencias
- Aplica migraciones
- Ejecuta los tests con `python manage.py test`
