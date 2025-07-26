from pydantic import BaseModel
from pydantic.alias_generators import to_camel

class CamelModel(BaseModel):
  class Config:
    alias_generator = to_camel
    validate_by_name = True
