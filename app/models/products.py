from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String, ForeignKey, Integer
from app.backend.db import Base

class Products(Base):
    __tablename__ = "products"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(60))
    slug:Mapped[str] = mapped_column(String(60), unique=True, index=True)
    description:Mapped[str] = mapped_column(String(200))
    price:Mapped[int] = mapped_column(Integer())
    stock:Mapped[int] = mapped_column(Integer())
    category_id:Mapped[int] = mapped_column(Integer(), ForeignKey("category.id"))
    is_active:Mapped[bool] = mapped_column(Boolean(), default=True)

    category = relationship("Category", back_populates='products', uselist=False)


