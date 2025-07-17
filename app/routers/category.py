from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated
from sqlalchemy import insert, update
from slugify import slugify

from app.backend.db_depends import get_db
from app.schema import CreateCategory
from app.models.category import Category
from app.models.products import Products


router = APIRouter(prefix="/category", tags=["category"])


@router.get("/")
async def get_all_categories(db: Annotated[Session, Depends(get_db)]):
    categories = db.scalars(select(Category).where(Category.is_active == True)).all()
    return categories

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(db: Annotated[Session, Depends(get_db)], create_category: CreateCategory)->dict:
    db.execute(
        insert(Category).values(
            name=create_category.name,
            #parent_id=create_category.parent_id,
            slug=slugify(create_category.name)
            )
    )
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "message": "success"
    }

@router.delete("/category_slug")
async def delete_category(db: Annotated[Session, Depends(get_db)], category_slug: str):
    category = db.scalars(select(Category).where(Category.slug == category_slug, Category.is_active == True))
    if category is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    db.execute(update(Category).where(Category.slug == category_slug).values(is_active=False))
    db.commit()
    return{
        "status_code" : status.HTTP_200_OK,
        "transaction": "Category delete is Successful"
    }