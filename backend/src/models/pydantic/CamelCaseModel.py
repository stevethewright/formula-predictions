from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel

class CamelCaseModel(SQLModel):
  class Config(): # type: ignore # TODO: Anyway to do this better?
    alias_generator = to_camel
    validate_by_name = True 
    from_attributes = True
