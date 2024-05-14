from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from sqlalchemy import asc
from sqlalchemy.orm import Session
from db.session import get_db
from models.access_road import AccessRoad


access_road_route = APIRouter()


@access_road_route.get(
    "/access_road",
    tags=["Access Road"],
    summary="Get Tourists by Autonomous Community",
    description="Get all Tourists by Autonomous Community in Spain"
)
def tourists_access_route(access_road_type: str, data_type: str = "Dato base", db: Session = Depends(get_db)):
    result = db.query(AccessRoad).filter(AccessRoad.access_road_type.ilike(f'%{access_road_type}%'), AccessRoad.data_type.like(f'%{data_type}%')).order_by(asc(AccessRoad.year), asc(AccessRoad.month)).all()
    if len(result) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No data has been found for the indicated access road type")
    data = []
    for item in result:
        date = datetime(item.year, item.month, 1)
        iso_date = date.isoformat().split('T')[0]
        value = item.total
        if "variación" in data_type:
            value = round(item.total / 100, 2)
        data.append({
            "access_road_type": item.access_road_type,
            "time": iso_date,
            "value": value
        })
    db.close()
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data, status_code=status.HTTP_200_OK)
