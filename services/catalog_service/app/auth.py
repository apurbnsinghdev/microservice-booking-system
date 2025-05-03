from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from typing import Dict
import os

# OAuth2PasswordBearer helps in extracting the token from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key and algorithm for JWT token generation and verification
SECRET_KEY = os.getenv("SECRET_KEY", "123456")
ALGORITHM = "HS256"

class User(BaseModel):
    username: str
    role: str

class TokenData(BaseModel):
    username: str
    role: str

def skip_admin_required():
    return

# Function to decode and get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = TokenData(**payload)
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Dependency to check if the current user has admin role
def admin_required(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user
