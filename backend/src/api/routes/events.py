from fastapi import APIRouter
from api.models.Event import Event
import fastf1

router = APIRouter()
schedule_remaining = fastf1.get_events_remaining()

@router.get("/next")
def get_next_event():
  if schedule_remaining.__len__() > 0:
    next = schedule_remaining.iloc[0]
    next_event = Event(
      round_number=next["RoundNumber"],
      country=next["Country"],
      location=next["Location"],
      official_event_name=next["OfficialEventName"],
      event_name=next["EventName"],
      event_date=next["EventDate"].to_pydatetime(),
      event_format=next["EventFormat"],
      session1=next["Session1"],
      session1_date=next["Session1Date"].to_pydatetime(),
      session1_date_utc=next["Session1DateUtc"].to_pydatetime(),
      session2=next["Session2"],
      session2_date=next["Session2Date"].to_pydatetime(),
      session2_date_utc=next["Session2DateUtc"].to_pydatetime(),
      session3=next["Session3"],
      session3_date=next["Session3Date"].to_pydatetime(),
      session3_date_utc=next["Session3DateUtc"].to_pydatetime(),
      session4=next["Session4"],
      session4_date=next["Session4Date"].to_pydatetime(),
      session4_date_utc=next["Session4DateUtc"].to_pydatetime(),
      session5=next["Session5"],
      session5_date=next["Session5Date"].to_pydatetime(),
      session5_date_utc=next["Session5DateUtc"].to_pydatetime(),
      f1_api_support=next["F1ApiSupport"]
    )
    return next_event
  return {"Error": "No remaining events."}
