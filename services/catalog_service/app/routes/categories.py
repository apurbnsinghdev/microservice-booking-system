from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Category, CategoryCreate, CategoryRead
from app.database import get_db_session
from app.auth import skip_admin_required

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryRead, dependencies=[Depends(skip_admin_required)])
def create_category(category_in_data: CategoryCreate, session: Session = Depends(get_db_session)):
    category = Category.from_orm(category_in_data)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

@router.get("/", response_model=List[CategoryRead])
def list_categories(session: Session = Depends(get_db_session)):
    try:
        categories = session.exec(select(Category)).all()
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve categories")

@router.get("/ping")
def ping(session: Session = Depends(get_db_session)):
    return {"message": "pong"}
