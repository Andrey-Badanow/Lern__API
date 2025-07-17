from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base
from sqlalchemy import String, Boolean
from app.models.products import Products


class Category(Base):
    __tablename__ = 'category'
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(60))
    slug:Mapped[str] = mapped_column(String(60), index=True, unique=True)
    is_active:Mapped[bool] = mapped_column(Boolean(), default=True)

    products = relationship("Products", back_populates='category', uselist=True)



if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Category.__table__))
    print(CreateTable(Products.__table__))