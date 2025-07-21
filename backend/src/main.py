from fastapi import FastAPI
from api.routes.events import router as events_router

app = FastAPI()

app.include_router(events_router, prefix="/events")

@app.get("/")
async def root():
  return {"message": "Formula Predictions Backend"}
