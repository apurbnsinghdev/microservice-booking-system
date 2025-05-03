from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import SubCategory, SubCategoryCreate, SubCategoryRead
from app.database import get_db_session
from app.auth import skip_admin_required

router = APIRouter(prefix="/subcategories", tags=["SubCategories"])

@router.post("/", response_model=SubCategoryRead, dependencies=[Depends(skip_admin_required)])
def create_subcategory(subcategory_in: SubCategoryCreate, session: Session = Depends(get_db_session)):
    subcategory = SubCategory.from_orm(subcategory_in)
    session.add(subcategory)
    session.commit()
    session.refresh(subcategory)
    return subcategory

@router.get("/", response_model=List[SubCategoryRead])
def list_subcategories(session: Session = Depends(get_db_session)):
    try:
        subcategories = session.exec(select(SubCategory)).all()
        return subcategories
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve subcategories")
