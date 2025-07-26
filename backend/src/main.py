from fastapi import FastAPI
from api.health.routes import router as health_router
from api.events.routes import router as events_router

app = FastAPI()

app.include_router(health_router, prefix="/health")
app.include_router(events_router, prefix="/events")

@app.get("/")
async def root():
  return {"message": "Formula Predictions Backend"}
