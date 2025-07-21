from fastapi import APIRouter
import fastf1

from api.models.Event import Event
from api.util.FormulaPredictionsUtils import pascal_to_snake

router = APIRouter()
schedule_remaining = fastf1.get_events_remaining()

@router.get("/next", response_model=Event)
def get_next_event():
  if schedule_remaining.__len__() > 0:
    next_dict = schedule_remaining.iloc[0].to_dict()
    next_normalised_dict = {
      pascal_to_snake(k): v for k, v in next_dict.items()
    }
    next_event = Event(**next_normalised_dict)
    return next_event
  return {"Error": "No remaining events."}
