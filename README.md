# 💰 Finance Dashboard Backend
### 🚀 Production-Ready Fintech API with FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=json-web-tokens)](https://jwt.io/)

---

## 📌 Overview
A production-grade backend system for managing financial records and real-time analytics. Built with **Clean Architecture** principles, this system is designed for high-stakes environments where security and data integrity are non-negotiable.

### 🛡️ Core Pillars
* **🔐 Strong Security:** OAuth2 with Password Hashing & JWT.
* **💰 Financial Data Integrity:** Decimal precision to avoid floating-point errors.
* **⚡ High Performance:** Optimized SQL aggregations with indexing.
* **🧱 Scalable Design:** Decoupled layers for easy maintenance.

---

## 🧠 Architecture
The project follows a strict **Clean Architecture** (Layered) pattern to separate business logic from the framework and database.

```mermaid
graph TD
    A[Client / Frontend] --> B[FastAPI Routes]
    B --> C[Service Layer]
    C --> D[Repository Layer]
    D --> E[(PostgreSQL Database)]
