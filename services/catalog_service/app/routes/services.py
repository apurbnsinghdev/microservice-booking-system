from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Service, ServiceCreate, ServiceRead
from app.database import get_db_session
from app.auth import admin_required

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=ServiceRead, dependencies=[Depends(admin_required)])
def create_service(service_insert: ServiceCreate, session: Session = Depends(get_db_session)):
    service = Service.from_orm(service_insert)
    session.add(service)
    session.commit()
    session.refresh(service)
    return service

@router.get("/", response_model=List[ServiceRead])
def list_services(session: Session = Depends(get_db_session)):
    try:
        services = session.exec(select(Service)).all()
        return services
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve services")
    
@router.get("/ping")
def ping(session: Session = Depends(get_db_session)):
    return {"message": "pong"}