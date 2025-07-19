from fastapi import APIRouter
import fastf1
from datetime import datetime

router = APIRouter()
schedule = fastf1.get_event_schedule(datetime.now().year)

@router.get("/next")
def get_next_race():
  return {"date": schedule.get_event_by_round(13).get_session_date('FP1')} 
