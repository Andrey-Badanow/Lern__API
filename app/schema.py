from pydantic import BaseModel, Field
from datetime import datetime
from fastapi import Query, Form

class CreateCategory(BaseModel):
    name: str = Field(description="Kategoriename", max_length=60)
    parent_id: int

