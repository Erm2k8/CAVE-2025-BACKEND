from fastapi import APIRouter, HTTPException, Depends, Response
from schemas import ReportCreate
from services.reports import ReportService
from .deps import get_reports_service

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

@router.post("/")
def create_report(report: ReportCreate, reports_service: ReportService = Depends(get_reports_service)):
    try:
        if report.format == "excel":
            excel_data = reports_service.get_report_excel()
            media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            headers = {
                'Content-Disposition': 'attachment; filename="report.xlsx"'
            }
            return Response(content=excel_data, media_type=media_type, headers=headers)

        elif report.format == "csv":
            csv_data = reports_service.get_report_csv()
            media_type = "text/csv"
            headers = {
                'Content-Disposition': 'attachment; filename="report.csv"'
            }
            return Response(content=csv_data, media_type=media_type, headers=headers)

        elif report.format == "json":
            json_data_string = reports_service.get_report_json()
            media_type = "application/json"
            return Response(content=json_data_string, media_type=media_type)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))