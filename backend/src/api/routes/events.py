from fastapi import APIRouter

router = APIRouter()

@router.get("/next")
def get_next_race():
  return {"test": "next_race"}
