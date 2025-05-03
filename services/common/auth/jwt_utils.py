from typing import List, Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("SECRET_KEY", "test_secret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def verify_jwt_token(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = {
                "sub": "user1",
                "role": "admin",
                "scopes": ["catalog:read", "catalog:write"]
            }
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def scopes_required(required_scopes: List[str]):
    #To Do
    return True


def role_required(required_role: str):
    #To Do
    return True
