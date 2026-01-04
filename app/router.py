from fastapi import APIRouter
from app.schemas import TicketRequest, TicketResponse
from app.services.classifier import classify_ticket
from app.services.router_engine import route_ticket
from app.services.summarizer import summarize_ticket

router = APIRouter()


@router.post("/process-ticket", response_model=TicketResponse)
def process_ticket(ticket: TicketRequest):
    category = classify_ticket(ticket.text)
    routed_to = route_ticket(category)
    summary = summarize_ticket(ticket.text)

    return TicketResponse(
        category=category,
        routed_to=routed_to,
        summary=summary
    )
