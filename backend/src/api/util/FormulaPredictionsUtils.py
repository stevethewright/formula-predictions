from datetime import datetime, timezone
import re

def pascal_to_snake(input: str) -> str:
  """
  Convert PascalCase string to a to snake_case.
  """
  return re.sub(r'(?<!^)(?=[A-Z])', '_', input).lower()

def pascal_dict_to_snake_dict(pascal_dict) -> dict:
  """
  Convert a PascalCase dictionary to a snake_case dictionary.
  """
  return { pascal_to_snake(k): v for k, v in pascal_dict.items() }

def current_utc_time():
  """
  Returns the current time in UTC.
  """
  return datetime.now(timezone.utc)
