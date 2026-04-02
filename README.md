
# 🚀 Fintech-Grade Finance Backend

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Status](https://img.shields.io/badge/status-production--ready-blue)
![Architecture](https://img.shields.io/badge/architecture-clean--architecture-orange)

---

## 🧠 Overview
A production-ready finance backend demonstrating **fintech-grade engineering practices**:
- Double-entry accounting
- Idempotent APIs
- JWT authentication
- Clean architecture

---

## 🏗️ Architecture
```
Client → API Layer → Service Layer → DB (SQLAlchemy)
```

---

## 🔐 Features
- JWT Authentication
- Role-based access (extendable)
- Immutable ledger (no updates/deletes)
- Idempotency key protection
- Aggregation dashboard APIs

---

## 📊 API
### Auth
- POST /v1/auth/register
- POST /v1/auth/login

### Records
- POST /v1/records (requires X-Idempotency-Key)

### Dashboard
- GET /v1/dashboard/summary

---

## 🚀 Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## ⚖️ Design Decisions
- SQL over NoSQL → ACID guarantees
- REST over GraphQL → simplicity
- JWT → stateless scaling
- Ledger → prevents financial corruption

---

## 🔥 Why This Stands Out
- Implements real fintech patterns
- Clean, modular code
- Interview-ready architecture
