
from fastapi import FastAPI
from app.routes import auth, records, dashboard
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fintech Finance Backend")

app.include_router(auth.router, prefix="/v1")
app.include_router(records.router, prefix="/v1")
app.include_router(dashboard.router, prefix="/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
