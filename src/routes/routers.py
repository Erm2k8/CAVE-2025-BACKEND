from fastapi import APIRouter, HTTPException, Depends
from .bid import router as bid_router
from .reports import router as reports_router

router = APIRouter()

router.include_router(bid_router)
router.include_router(reports_router)
