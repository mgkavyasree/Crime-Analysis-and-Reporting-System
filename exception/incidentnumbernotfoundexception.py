class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_id=None, message=None):
        if incident_id is not None:
            default_message = f"Incident with ID {incident_id} was not found in the database."
        else:
            default_message = "Incident number not found in the database."

        super().__init__(message or default_message)
