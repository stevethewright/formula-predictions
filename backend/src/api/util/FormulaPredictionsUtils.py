import re

# Convert PascalCase → snake_case
def pascal_to_snake(name):
  return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
