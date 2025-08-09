from fastapi import APIRouter, HTTPException, Depends
from schemas import UserLogin
from auth import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.get("/validate_auth")
async def validate_auth(current_user=Depends(get_current_user)):
    return { "status": "success", "message": "Login successful" }
