from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from db.session import get_db
from models.tourists import Tourists


tourists_route = APIRouter()


@tourists_route.get(
    "/tourists/{autonomous_community}",
    tags=["Tourists"],
    summary="Get Tourists by Autonomous Community",
    description="Get all Tourists by Autonomous Community in Spain"
)
def tourists_by_autonomous_community(autonomous_community: str, db: Session = Depends(get_db)):
    result = db.query(Tourists).filter(Tourists.autonomous_community.like(f'%{autonomous_community}%')).all()
    for item in result:
        print(item.autonomous_community, item.data_type, item.period, item.total)
    db.close()
    return Response(status_code=status.HTTP_200_OK)
