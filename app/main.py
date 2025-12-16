from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from sqlalchemy import text

app = FastAPI(title="Inventory Management API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to Inventory API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/db-test")
async def test_database(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        return {"status": "Database connected successfully", "result": result.scalar()}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}