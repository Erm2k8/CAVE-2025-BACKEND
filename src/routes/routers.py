from fastapi import APIRouter, HTTPException, Depends
from .bid import router as bid_router

router = APIRouter()

router.include_router(bid_router)
