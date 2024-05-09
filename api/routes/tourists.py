from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from db.session import get_db
from utils.statics import load_data_from_s3
from models.tourists import Tourists


tourists_route = APIRouter()


@tourists_route.get(
    "/database/tourists",
    tags=["Data"],
    summary="Tourists Database",
    description="Create Tourists Database"
)
def create_tourists_db(db: Session = Depends(get_db)):
    # df = load_data_from_s3()
    # for index, row in df.iterrows():
    #     if isinstance(row['Total'], float):
    #         total = row['Total']
    #     else:
    #         total_str = row['Total'].replace('.', '').replace(',', '')
    #         total = float(total_str) if total_str else 0.0
    #     turismo_entry = Tourists(
    #         comunidad_autonoma=row['Comunidades autónomas'],
    #         tipo_dato=row['Tipo de dato'],
    #         periodo=row['Periodo'],
    #         total=total
    #     )
    #     db.add(turismo_entry)
    # db.commit()
    # return Response(status_code=status.HTTP_201_CREATED)

    result = db.query(Tourists).filter(Tourists.comunidad_autonoma.like('%Canarias%')).all()
    for item in result:
        print(item.comunidad_autonoma, item.periodo, item.total)
    db.close()
    return Response(status_code=status.HTTP_200_OK)
