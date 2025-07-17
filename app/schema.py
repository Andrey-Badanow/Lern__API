from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    name: str = Field(description="Kategoriename", max_length=60)
    parent_id: int


class CreateProduct(BaseModel):
    name: str = Field(description="ProdukteName", max_length=60)
    description:str = Field(max_length=250)
    price:int
