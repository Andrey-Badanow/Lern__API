from fastapi import FastAPI
from app.routers.products import router as prod_router
from app.routers.category import router as cat_router

app = FastAPI()

@app.get("/")
async def welcome_page() -> str:
    return "Wilkommen, mein liebe Freund"

app.include_router(prod_router)
app.include_router(cat_router)