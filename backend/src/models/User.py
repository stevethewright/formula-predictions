from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from ..api.util.FormulaPredictionsUtils import current_utc_time
from .pydantic.CamelCaseModel import CamelCaseModel

class User(CamelCaseModel):
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  name: str
  favorite_driver_id: UUID = Field(foreign_key="driver.id")
  favorite_team_id: UUID = Field(foreign_key="team.id")
  created_at: datetime = Field(default_factory=current_utc_time)
  updated_at: datetime = Field(default_factory=current_utc_time)
