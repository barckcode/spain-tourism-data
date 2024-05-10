import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()


def get_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    correct_api_key = os.getenv("TURISM_DATA_API_KEY")
    if credentials.credentials != correct_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect API Key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials
