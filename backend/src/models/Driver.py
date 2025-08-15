from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from ..api.util.FormulaPredictionsUtils import current_utc_time
from .pydantic.CamelCaseModel import CamelCaseModel

class Driver(CamelCaseModel):
  id: UUID = Field(default_factory=uuid4, primary_key=True)
  first_name: str
  last_name: str
  team_id: UUID = Field(foreign_key='team.id')
  number: int
  nationality: str
  active: bool
  created_at: datetime = Field(default_factory=datetime.utcnow)
  updated_at: datetime = Field(default_factory=datetime.utcnow)
