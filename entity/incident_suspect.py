class IncidentSuspect:
    def __init__(self, incident_id=None, suspect_id=None):
        self.__incident_id = incident_id
        self.__suspect_id = suspect_id

    def get_incident_id(self):
        return self.__incident_id
    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def get_suspect_id(self):
        return self.__suspect_id
    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id

    @classmethod
    def sample_data(cls):
        return [
            cls(501, 401),
            cls(502, 402)
        ]
