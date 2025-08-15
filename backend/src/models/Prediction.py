from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from ..api.util.FormulaPredictionsUtils import current_utc_time
from .pydantic.CamelCaseModel import CamelCaseModel

class Prediction(CamelCaseModel):
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  user_id: UUID = Field(foreign_key="user.id")
  event_id: int
  session_id: int
  created_at: datetime = Field(default_factory=current_utc_time)
  updated_at: datetime = Field(default_factory=current_utc_time)
