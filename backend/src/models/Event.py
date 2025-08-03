from datetime import datetime

from .pydantic.CamelCaseModel import CamelCaseModel

class Event(CamelCaseModel):
  round_number: int
  country: str
  location: str
  official_event_name: str
  event_name: str
  event_date: datetime
  event_format: str
  session1: str
  session1_date: datetime
  session1_date_utc: datetime
  session2: str
  session2_date: datetime
  session2_date_utc: datetime
  session3: str
  session3_date: datetime
  session3_date_utc: datetime
  session4: str
  session4_date: datetime
  session4_date_utc: datetime
  session5: str
  session5_date: datetime
  session5_date_utc: datetime
  f1_api_support: bool
