# Sheba Booking System (Simplified)

This is a microservice-based system simulating Sheba's booking platform with:
- 🛒 Cart Service (FastAPI + PostgreSQL)
- 📚 Catalog Service (FastAPI + PostgreSQL)
- ⏰ Slot Service (FastAPI + Redis Cache)

## Features
- Microservices: Cart, Catalog, Slot
- JWT Auth (Roles: admin, customer)
- Checkout flow with slot availability check
- Redis caching for partner slots
- Swagger docs for all APIs

# 🛠️ Sheba Booking Microservices System (FastAPI + Docker + Redis + Postgres)

A simplified Service Booking System (like Sheba) built with **FastAPI microservices**:
- Cart Service (CRUD + Checkout + JWT)
- Catalog Service (Categories & Services)
- Slot Service (Partner slot availability with Redis cache)

---

## 📦 Microservices Overview

| Service        | Port  | Description                     |
|----------------|-------|----------------------------------|
| Cart Service   | 8001  | Cart CRUD, JWT Auth, Checkout    |
| Catalog Service| 8002  | Service listing (Category/Sub)   |
| Slot Service   | 8003  | Mock slot availability with Redis|

---

## 🚀 Tech Stack

- **FastAPI** (Python 3.10+)
- **PostgreSQL** (per service)
- **Redis** (slot caching)
- **Docker Compose** (or manual)
- **JWT Auth** (Roles: customer, admin)

---

## 🔥 Running the System (Docker Way)

1. **Clone the repo**

```bash
git clone https://github.com/yourname/sheba-booking-system.git
cd sheba-booking-system
```
2. **Copy envs & adjust them**
```
cp cart_service/.env.sample cart_service/.env
cp catalog_service/.env.sample catalog_service/.env
cp slot_service/.env.sample slot_service/.env
```
3. **Copy envs & adjust them**
```
docker-compose up --build
```

3. **Access services**
Cart Service: http://localhost:8000/docs

Catalog Service: http://localhost:8001/docs

Slot Service: http://localhost:8002/docs```


4. **Database Migration & Seeding**
```
docker exec -it catalog_service alembic upgrade head

```

5. **Seed data**
```
docker exec -it catalog_service python seed.py

```