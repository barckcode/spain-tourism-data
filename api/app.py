import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.database import database_route
from routes.tourists import tourists_route
from routes.access_road import access_road_route
from routes.accommodation_type import accommodation_type_route


spain_turism_frontend = os.getenv('SPAIN_TURISM_FRONTEND')


app = FastAPI(
    title="Tourism in Spain",
    description="Tourism in Spain explained with data",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Data",
            "description": "Manage API Data"
        },
        {
            "name": "Tourists",
            "description": "Tourists in Spain"
        },
        {
            "name": "Access Road",
            "description": "Types of tourist access to Spain"
        },
        {
            "name": "Accommodation Type",
            "description": "Types of accommodation chosen by tourists."
        },
        {
            "name": "Travel Time",
            "description": "Travel time to the tourist destination."
        }
    ]
)

origins = [
    spain_turism_frontend,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(database_route)
app.include_router(tourists_route)
app.include_router(access_road_route)
app.include_router(accommodation_type_route)
