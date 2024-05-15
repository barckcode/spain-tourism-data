from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from sqlalchemy import asc
from sqlalchemy.orm import Session
from db.session import get_db
from models.accommodation_type import AccommodationType


accommodation_type_route = APIRouter()


@accommodation_type_route.get(
    "/accommodation-type",
    tags=["Accommodation Type"],
    summary="Get Accommodation Type Data",
    description="Get all Accommodation Type Data in Spain"
)
def get_accommodation_type_data(accommodation_type_name: str, paid_accommodation: str, data_type: str = "Dato base", db: Session = Depends(get_db)):
    result = db.query(AccommodationType).filter(AccommodationType.accommodation_type_name == accommodation_type_name, AccommodationType.paid_accommodation == paid_accommodation, AccommodationType.data_type.like(f'%{data_type}%')).order_by(asc(AccommodationType.year), asc(AccommodationType.month)).all()
    if len(result) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No data has been found for the indicated accommodation type")
    data = []
    for item in result:
        date = datetime(item.year, item.month, 1)
        iso_date = date.isoformat().split('T')[0]
        value = item.total
        if "variación" in data_type:
            value = round(item.total / 100, 2)
        data.append({
            "accommodation_type_name": item.accommodation_type_name,
            "paid_accommodation": item.paid_accommodation,
            "time": iso_date,
            "value": value
        })
    db.close()
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data, status_code=status.HTTP_200_OK)
