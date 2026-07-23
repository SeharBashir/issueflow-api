class HealthService:
    """
    Handles application health information.
    """

    def get_status(self) -> dict:
        return {
            "status": "healthy",
            "service": "issueflow-api"
        }