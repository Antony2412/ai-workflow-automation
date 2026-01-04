from pydantic import BaseModel, Field


class TicketRequest(BaseModel):
    """
    Incoming support ticket request.
    """
    text: str = Field(
        ...,
        min_length=5,
        description="Raw support ticket text submitted by user"
    )


class TicketResponse(BaseModel):
    """
    Processed ticket response returned by the system.
    """
    category: str = Field(
        ...,
        description="Predicted ticket category"
    )
    routed_to: str = Field(
        ...,
        description="Enterprise team the ticket is routed to"
    )
    summary: str = Field(
        ...,
        description="Concise AI-generated summary of the ticket"
    )
