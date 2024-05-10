from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from db.session import get_db
from utils.statics import load_data_from_s3
from utils.clean_data import clean_autonomous_community_name
from auth.api_key import get_api_key
from models.tourists import Tourists


database_route = APIRouter()


@database_route.get(
    "/database/tourists",
    tags=["Data"],
    summary="Tourists Database",
    description="Create Tourists Database",
    dependencies=[Depends(get_api_key)]
)
def create_tourists_db(db: Session = Depends(get_db)):
    df = load_data_from_s3()
    for _, row in df.iterrows():
        if isinstance(row['Total'], float):
            total = row['Total']
        else:
            total_str = row['Total'].replace('.', '').replace(',', '')
            total = float(total_str) if total_str else 0.0
        autonomous_community = clean_autonomous_community_name(row['Comunidades autónomas'])
        year, month = row['Periodo'].split('M')
        turismo_entry = Tourists(
            autonomous_community=autonomous_community,
            data_type=row['Tipo de dato'],
            year=int(year),
            month=int(month),
            total=total
        )
        db.add(turismo_entry)
    db.commit()
    return Response(status_code=status.HTTP_201_CREATED, content="Database of Tourists in Spain Created")
