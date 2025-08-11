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
        
        df = df.rename(columns={
            "amount": "Valor",
            "cpf": "CPF",
            "phone": "Telefone",
            "name": "Nome"
        })
        
        # Ordena pelo valor do lance
        df = df.sort_values(by='Valor', ascending=False)
        
        # Formatação dos campos
        df['Valor'] = df['Valor'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
        df['CPF'] = df['CPF'].apply(lambda x: f'{x[:3]}.{x[3:6]}.{x[6:9]}-{x[9:]}')
        df['Telefone'] = df['Telefone'].apply(lambda x: f'({x[:2]}) {x[2:7]}-{x[7:]}')
        df['Nome'] = df['Nome'].apply(lambda x: x.title())
                
        output_buffer = io.BytesIO()
        df.to_excel(output_buffer, index=False, engine='openpyxl')
        excel_data = output_buffer.getvalue()
        
        return excel_data
    
    @staticmethod
    def get_report_json() -> List[dict[str, Any]]:
        df = ReportService.get_report()
        json_data = df.to_json(orient='records')
        return json_data
    