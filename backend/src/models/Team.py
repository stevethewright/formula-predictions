from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field

from ..api.util.FormulaPredictionsUtils import current_utc_time
from .pydantic.CamelCaseModel import CamelCaseModel

class Team(CamelCaseModel):
  team_id: UUID = Field(default_factory=uuid4, primary_key=True)
  name: str
  nationality: str
  team_principal: str
  active: bool
  created_at: datetime = Field(default_factory=datetime.utcnow)
  updated_at: datetime = Field(default_factory=datetime.utcnow)
