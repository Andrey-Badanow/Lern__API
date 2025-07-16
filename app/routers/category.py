from fastapi import APIRouter


router = APIRouter(prefix="/category", tags=["category"])


@router.get("/")
async def all_category():
    return "Alle Kategorien"