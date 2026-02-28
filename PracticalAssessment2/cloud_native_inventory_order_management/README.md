# Cloud-Native Inventory & Order Management System

A project using:

- FastAPI backend
- SQLAlchemy ORM
- Alembic migrations
- MySQL for SQL data
- MongoDB for activity logs only
- Pure HTML + Bootstrap 5 UI with fetch-based API calls

This system supports **MySQL (SQL)** and **MongoDB (NoSQL)**.

## Project Structure

```
cloud_native_inventory_order_management/
├── src/
│   ├── api/
│   ├── db/
│   ├── services/
│   ├── config.py
│   ├── dependencies.py
│   ├── main.py
│   ├── schemas.py
│   └── seed.py
├── db/
│   ├── alembic.ini
│   └── migrations/
├── ui/
│   ├── css/
│   ├── js/
│   ├── index.html
│   ├── users.html
│   ├── products.html
│   ├── inventory.html
│   ├── orders.html
│   └── logs.html
├── docker/
├── tests/
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features

- CRUD APIs for `Users`, `Products`, `Inventory`, `Orders`, `OrderItems`
- MongoDB-based Activity Logs API
- Health-check endpoint: `/health`
- Seed data script
- Bootstrap pages:
  - Home
  - Register
  - Sign In
  - Users Management
  - Products Management
  - Inventory Management
  - Order Creation + Order Details
  - Activity Logs Viewer

## Setup (Local)

1. Create and activate virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy env file:
   ```bash
   copy .env.example .env
   ```
4. Run API:
   ```bash
   uvicorn src.main:app --reload
   ```
5. Open browser:
   - `http://127.0.0.1:8000/`

## Docker Setup (Recommended)

```bash
docker compose up --build
```

Services started:

- API: `http://localhost:8000`
- MySQL: `localhost:3306`
- MongoDB: `localhost:27017`

## Seed Data

```bash
python -m src.seed
```

## Alembic Commands

```bash
alembic -c db/alembic.ini upgrade head
alembic -c db/alembic.ini downgrade -1
```

## API Quick List

- `GET /health`
- `GET/POST /api/users/`
- `GET/PUT/DELETE /api/users/{id}`
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET/POST /api/products/`
- `GET/PUT/DELETE /api/products/{id}`
- `GET/POST /api/inventory/`
- `GET/PUT/DELETE /api/inventory/{id}`
- `GET/POST /api/orders/`
- `GET /api/orders/{id}`
- `PATCH /api/orders/{id}/status`
- `DELETE /api/orders/{id}`
- `GET/POST /api/order-items/`
- `GET/PUT/DELETE /api/order-items/{id}`
- `GET/POST /api/logs/`

## Tests

```bash
pytest -q
```

Tests are intentionally simple for student-level submissions.
