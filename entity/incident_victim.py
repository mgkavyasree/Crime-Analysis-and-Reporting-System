class IncidentVictim:
    def __init__(self, incident_id=None, victim_id=None):
        self.__incident_id = incident_id
        self.__victim_id = victim_id

    def get_incident_id(self):
        return self.__incident_id
    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def get_victim_id(self):
        return self.__victim_id
    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    @classmethod
    def sample_data(cls):
        return [
            cls(501, 301),
            cls(502, 302)
        ]
