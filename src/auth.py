from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
import secrets
import os
from hashlib import sha256

security = HTTPBasic()

def get_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = os.getenv("ADMIN_USERNAME").encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    
    current_password_bytes = credentials.password.encode("utf8")
    hashed_password = sha256(current_password_bytes).hexdigest().encode("utf8")
    correct_password_bytes = os.getenv("ADMIN_HASHED_PASSWORD").encode("utf8")
    is_correct_password = secrets.compare_digest(
        hashed_password, correct_password_bytes
    )
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
        
    return credentials.username