#Business routing logic is decoupled from ML predictions, enabling policy updates without retraining models.
def route_ticket(category: str) -> str:
    """
    Route ticket to appropriate enterprise team based on category.
    """
    routing_table = {
        "IT": "IT Support Team",
        "HR": "HR Operations Team",
        "Finance": "Finance Desk"
    }

    return routing_table.get(category, "General Support")
