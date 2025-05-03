# Booking System

This is a microservice-based system testing project for xyz booking platform with:
- Cart Service (FastAPI + PostgreSQL)
- Catalog Service (FastAPI + PostgreSQL)
- Slot Service (FastAPI + Redis Cache)

## Features
- Microservices: Cart, Catalog, Slot
- JWT Auth (Roles: admin, customer)
- Checkout flow with slot availability check
- Redis caching for partner slots
- Swagger docs for all APIs

# Microservices Booking System (FastAPI + Docker + Redis + Postgres)

**FastAPI microservices**:
- Cart Service (CRUD + Checkout + JWT)
- Catalog Service (Categories & Services)
- Slot Service (Partner slot availability with Redis cache)

---

## Microservices Overview

Cart Service 
    - runing on port 8000
    - Cart CRUD, JWT Auth, Checkout
Catalog Service 
    - running on port 8001
    - Service listing (Category/Sub)
    - 
Slot Service 
    - running on port 80002
    - Mock slot availability with Redis
---

## Tech Stack

- **FastAPI** (Python 3.10+)
- **PostgreSQL** (per service)
- **Redis** (slot caching)
- **Docker Compose** (or manual)
- **JWT Auth** (Roles: customer, admin)

---

## Running the System (Docker Way)

1. **Clone the repo**

```bash
git clone https://github.com/apurbnsinghdev/microservice-booking-system.git
cd microservice-booking-system
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
[Cart Service:] (http://localhost:8000/docs)

[Catalog Service:] (http://localhost:8001/docs)

[Slot Service:] (http://localhost:8002/docs)

4. **Database Migration & Seeding**
```
docker exec -it catalog_service alembic upgrade head

```

5. **Seed data**
```
docker exec -it catalog_service python seed.py

```

---

# Architecture & ERD

## Microservice Overview
- Cart Service: Handles cart CRUD, checkout, order saving.
- Catalog Service: Manages categories, subcategories, and service listings.

- Partner Slot Service: Manages partner availability (Redis-cached).
- REST-only API calls between services.

[CART SERVICE]
Cart (id, customer_id, created_at)
CartItem (id, cart_id, service_id, quantity)

[CATALOG SERVICE]
Category (id, name)
Subcategory (id, category_id, name)
Service (id, subcategory_id, name, price, description)

[SLOT SERVICE]
PartnerSlot (id, service_id, partner_id, slot_time, is_available)

[CHECKOUT]
Booking (id, cart_id, service_id, slot_id, order_id, discount, final_price, created_at)
----