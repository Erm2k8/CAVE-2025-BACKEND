from db import FirestoreDB
from .utils import Cleaner
from schemas import BidCreate
import uuid
from db import db

class BidsService:
    def create_bid(self, bid: BidCreate) -> None:
        bid_dict = bid.model_dump()
        bid_id = str(uuid.uuid4())
        bid_dict["cpf"] = Cleaner.clean_cpf(bid_dict["cpf"])
        bid_dict["phone"] = Cleaner.clean_phone(bid_dict["phone"])
        bid_dict["name"] = Cleaner.clean_name(bid_dict["name"])
        FirestoreDB.add_document("bids", bid_dict, doc_id=bid_id)


    def get_bids(self) -> list:
        return FirestoreDB.get_documents("bids")
    
    
    @staticmethod
    def get_bid_by_id(bid_id: str) -> dict:
        return FirestoreDB.get_document("bids", bid_id)
    
    
    @staticmethod
    def delete_all_bids() -> int:
        bids_ref = db.collection("bids")
        docs = bids_ref.stream() 
        
        deleted_count = 0
        batch = db.batch()
        
        for doc in docs:
            batch.delete(doc.reference)
            deleted_count += 1
            
            if deleted_count % 500 == 0:
                batch.commit()
                batch = db.batch() 

        if deleted_count % 500 != 0:
            batch.commit()
            
        return deleted_count
    
    
    @staticmethod
    def get_highest_bid() -> dict | None:
        bids_ref = db.collection("bids")

        query = bids_ref.order_by("amount", direction="DESCENDING").limit(1)
        
        results = query.stream()
        
        try:
            highest_bid = next(results)
            return highest_bid.to_dict()
        except StopIteration:
            return None
