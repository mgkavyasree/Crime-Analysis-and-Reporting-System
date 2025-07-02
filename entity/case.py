class Case:
    def __init__(self, caseid: int, casedescription: str, incidents: list = None):
        self.caseid = caseid
        self.casedescription = casedescription
        self.incidents = incidents if incidents is not None else []

    def get_caseid(self):
        return self.caseid

    def get_casedescription(self):
        return self.casedescription

    def get_incidents(self):
        return self.incidents

    def set_caseid(self, caseid: int):
        self.caseid = caseid

    def set_casedescription(self, casedescription: str):
        self.casedescription = casedescription

    def set_incidents(self, incidents: list):
        self.incidents = incidents

    @classmethod
    def sample_data(cls):
        from entity.incident import Incident
        return [
            cls(801, "Robbery Case", [Incident(501)]),
            cls(802, "Assault Case", [Incident(502)])
        ]
