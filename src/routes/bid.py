from fastapi import APIRouter, HTTPException, Depends
from schemas import BidCreate
from .deps import get_bids_service

router = APIRouter(
    prefix="/bids",
    tags=["Bids"],
)

@router.get("/")
async def read_bids(bids_service=Depends(get_bids_service)):
    return bids_service.get_bids()


@router.post("/")
async def create_bid(bid: BidCreate, bids_service=Depends(get_bids_service)):
    try:
        bids_service.create_bid(bid)
        return { "status": "success", "message": "Lance criado com sucesso" }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/")
async def delete_all_bids(bids_service=Depends(get_bids_service)):
    del_count = bids_service.delete_all_bids()
    return { "status": "success", "message": f"{del_count} lances foram deletados" }