from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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
    result = db.query(Tourists).filter(Tourists.autonomous_community.like(f'%{autonomous_community}%'), Tourists.data_type.like('%Dato base%')).all()
    if len(result) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No data has been found for the indicated autonomous community")
    data = []
    for item in result:
        data.append({
            "autonomous_community": item.autonomous_community,
            "year": item.year,
            "month": item.month,
            "total": item.total
        })
    db.close()
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data, status_code=status.HTTP_200_OK)
