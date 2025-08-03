from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from models import Event
from api.health.routes import router as health_router
from api.events.routes import router as events_router

@asynccontextmanager
async def lifespan(app: FastAPI):
  SQLModel.metadata.create_all(engine)
  yield

app = FastAPI(lifespan=lifespan)

app.include_router(health_router, prefix="/health")
app.include_router(events_router, prefix="/events")

@app.get("/")
async def root():
  return {"message": "Formula Predictions Backend"}
