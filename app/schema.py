from pydantic import BaseModel, Field


class CreateCategory(BaseModel):
    name: str = Field(description="Kategoriename", max_length=60)
    parent_id: int

