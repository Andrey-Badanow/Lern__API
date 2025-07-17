from fastapi import APIRouter, Depends, status, HTTPException
from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import insert, update, select
from app.schema import CreateProduct
from app.models.products import Products
from slugify import slugify


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def get_all_products(db:Annotated[Session, Depends(get_db)],
                           
                           ):
    products = db.scalars(select(Products).where(Products.is_active==True, 
                                      Products.stock > 0)).all()
    return products

@router.post("/{category_id}/create_products", status_code=status.HTTP_201_CREATED)
async def Create_Product(db: Annotated[Session, Depends(get_db)], 
                         create_prod:CreateProduct,
                         category_id: int):
    db.execute(
        insert(Products).values(
            name=create_prod.name, 
            slug=slugify(create_prod.name),
            description=create_prod.description,
            price=create_prod.price,
            stock=12,
            category_id=category_id,
            )
    )
    db.commit()
    return {"status_code": status.HTTP_201_CREATED,
            "message": "success"}

@router.delete("/{product_slug}", status_code=status.HTTP_418_IM_A_TEAPOT)
async def Delete_Product(db: Annotated[Session, Depends(get_db)], 
                         product_slug: str):
    product = db.scalars(select(Products).where(Products.slug == product_slug, 
                                                Products.is_active == True))
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Produkt nicht gefunden")
    db.execute(
        update(Products).where(Products.slug == product_slug).values(is_active=False)
    )
    db.commit()
    return {"status_code": status.HTTP_200_OK,
            "message": "Produkt erfolgreich entfernt"}