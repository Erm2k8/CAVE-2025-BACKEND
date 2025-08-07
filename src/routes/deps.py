from services.bids import BidsService
from services.reports import ReportService

def get_bids_service() -> BidsService:
    return BidsService()


def get_reports_service() -> ReportService:
    return ReportService()

