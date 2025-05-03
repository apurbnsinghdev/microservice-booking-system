from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
import sqlalchemy as sa

#======== CATEGORY SCHEMAS =====
class CategoryBase(SQLModel):
    name: str

class CategoryRead(CategoryBase):
    id: int

class CategoryCreate(CategoryBase):
    pass

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))
    subcategories: List["SubCategory"] = Relationship(back_populates="category")

#======== SUBCATEGORY SCHEMAS =====
class SubCategoryBase(SQLModel):
    name: str
    category_id: int

class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategoryRead(SubCategoryBase):
    id: int

class SubCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))
    category_id: int = Field(foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="subcategories")
    services: List["Service"] = Relationship(back_populates="subcategory")

#======== Service SCHEMAS =====
class ServiceBase(SQLModel):
    name: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))
    description: Optional[str] = Field(default=None, sa_column=sa.Column(sa.Text))
    price: float = Field(sa_column=sa.Column(sa.Float, nullable=False))

class ServiceCreate(ServiceBase):
    subcategory_id: int

class ServiceRead(ServiceBase):
    id: int
    subcategory_id: int

class Service(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=sa.Column(sa.String(255), nullable=False))
    description: Optional[str] = Field(
        default=None,
        sa_column=sa.Column(sa.Text(), nullable=True)
    )
    price: float = Field(sa_column=sa.Column(sa.Float(), nullable=False))
    subcategory_id: int | None = Field(default=None, foreign_key="subcategory.id")
    subcategory: Optional[SubCategory] = Relationship(back_populates="services")
