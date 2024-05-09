from fastapi import FastAPI
from routes.database import database_route
from routes.tourists import tourists_route


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
    ]
)

app.include_router(database_route)
app.include_router(tourists_route)
