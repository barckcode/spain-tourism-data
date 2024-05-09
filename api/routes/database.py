from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from db.session import get_db
from utils.statics import load_data_from_s3
from models.tourists import Tourists


database_route = APIRouter()


@database_route.get(
    "/database/tourists",
    tags=["Data"],
    summary="Tourists Database",
    description="Create Tourists Database"
)
def create_tourists_db(db: Session = Depends(get_db)):
    df = load_data_from_s3()
    for index, row in df.iterrows():
        if isinstance(row['Total'], float):
            total = row['Total']
        else:
            total_str = row['Total'].replace('.', '').replace(',', '')
            total = float(total_str) if total_str else 0.0
        turismo_entry = Tourists(
            autonomous_community=row['Comunidades autónomas'],
            data_type=row['Tipo de dato'],
            period=row['Periodo'],
            total=total
        )
        db.add(turismo_entry)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED, content="Database of Tourists in Spain Created")
