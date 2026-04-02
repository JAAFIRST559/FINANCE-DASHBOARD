# 💰 Finance Dashboard Backend (Fintech-Grade)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

------------------------------------------------------------------------

## 🚀 Overview

A **production-ready fintech backend** built with **FastAPI**,
implementing:

-   🔐 JWT Authentication + RBAC
-   💳 Financial Transactions
-   📊 Analytics & Dashboard APIs
-   ⚡ Redis Caching
-   🔁 Idempotency (no duplicate transactions)
-   🧾 Audit Logging

------------------------------------------------------------------------

## 🧠 Architecture

``` mermaid
graph TD
    A[Client / Frontend] --> B[FastAPI Routes]
    B --> C[Auth Middleware (JWT + RBAC)]
    C --> D[Service Layer]
    D --> E[Repository Layer]
    E --> F[(PostgreSQL DB)]
    D --> G[(Redis Cache)]
    D --> H[Idempotency Store]
    D --> I[Audit Logs]
```

------------------------------------------------------------------------

## 📸 API Documentation UI

Once the server is running:

-   Swagger UI → http://localhost:8000/docs
-   ReDoc → http://localhost:8000/redoc

------------------------------------------------------------------------

## 📬 API Endpoints

### 🔐 Auth

-   `POST /auth/register`
-   `POST /auth/login`

### 💳 Records

-   `GET /records/`
-   `POST /records/`
-   `DELETE /records/{id}`

### 📊 Dashboard

-   `GET /dashboard/summary`
-   `GET /dashboard/trends`
-   `GET /dashboard/categories`

------------------------------------------------------------------------

## 🛠️ Setup

### 1. Clone Repo

    git clone <repo-url>
    cd finance_backend

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Run Server

    uvicorn app.main:app --reload

------------------------------------------------------------------------

## 🐳 Docker

    docker-compose up --build

------------------------------------------------------------------------

## ⚙️ Environment Variables

    DATABASE_URL=postgresql://user:password@localhost:5432/finance
    SECRET_KEY=your_secret_key
    REDIS_HOST=localhost

------------------------------------------------------------------------

## 📬 Postman Collection

Import:

    postman_collection.json

------------------------------------------------------------------------

## ⚡ Fintech Features

### 🔁 Idempotency

Prevents duplicate transactions using:

    X-Idempotency-Key

### 🧾 Audit Logs

Tracks: - User actions - Timestamp - Changes

### ⚡ Redis

Used for: - Caching - Token blacklist - Idempotency tracking

------------------------------------------------------------------------

## 🚀 CI/CD

GitHub Actions pipeline: - Install dependencies - Run checks

------------------------------------------------------------------------

## ⚖️ Trade-offs & Design Decisions

  Decision            Reason
  ------------------- --------------------------------
  REST over GraphQL   Simpler & predictable
  PostgreSQL          ACID compliance
  JWT                 Stateless scaling
  Monolith            Easier to maintain early-stage

------------------------------------------------------------------------

## ❗ Limitations

-   No multi-currency support
-   No background job processing
-   No event streaming

------------------------------------------------------------------------

## 📈 Future Improvements

-   Kafka for event streaming
-   Celery for background jobs
-   Multi-currency support

------------------------------------------------------------------------

## 👨‍💻 Author

Built as a **production-grade fintech backend system** 🚀
