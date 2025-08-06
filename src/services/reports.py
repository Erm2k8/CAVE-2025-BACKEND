import io
from typing import Any, List
import pandas as pd
from db import FirestoreDB

class ReportService:
    @staticmethod
    def get_report() -> pd.DataFrame:
        bids = FirestoreDB.get_documents("bids")
        df = pd.DataFrame(bids)
        return df
    
    @staticmethod
    def get_report_csv() -> str:
        df = ReportService.get_report()
        csv_data = df.to_csv(index=False)
        return csv_data
    
    @staticmethod
    def get_report_excel() -> bytes:
        df = ReportService.get_report()
        output_buffer = io.BytesIO()
        
        df.to_excel(output_buffer, index=False, engine='openpyxl')   
        excel_data = output_buffer.getvalue()
        
        return excel_data
    
    @staticmethod
    def get_report_json() -> List[dict[str, Any]]:
        df = ReportService.get_report()
        json_data = df.to_json(orient='records')
        return json_data
    