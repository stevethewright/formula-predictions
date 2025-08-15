from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel

class CamelCaseModel(SQLModel):
  class Config(): # type: ignore
    alias_generator = to_camel
    validate_by_name = True 
    from_attributes = True
