from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from ..api.util.FormulaPredictionsUtils import current_utc_time
from .pydantic.CamelCaseModel import CamelCaseModel

class PredictedPosition(CamelCaseModel):
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  prediction_id: UUID = Field(foreign_key="prediction.id")
  predicted_position: int
  driver_id: UUID = Field(foreign_key="driver.id")
  created_at: datetime = Field(default_factory=datetime.utcnow)
  updated_at: datetime = Field(default_factory=datetime.utcnow)
