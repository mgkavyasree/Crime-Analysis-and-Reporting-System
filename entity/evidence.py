class Evidence:
    def __init__(self, evidenceid=None, description=None, locationfound=None, incidentid=None):
        self.evidenceid = evidenceid
        self.description = description
        self.locationfound = locationfound
        self.incidentid = incidentid

    def get_evidenceid(self):
        return self.evidenceid

    def get_description(self):
        return self.description

    def get_locationfound(self):
        return self.locationfound

    def get_incidentid(self):
        return self.incidentid

    def set_evidenceid(self, evidenceid):
        self.evidenceid = evidenceid

    def set_description(self, description):
        self.description = description

    def set_locationfound(self, locationfound):
        self.locationfound = locationfound

    def set_incidentid(self, incidentid):
        self.incidentid = incidentid

    @classmethod
    def sample_data(cls):
        return [
            cls(601, 'Bike key found', 'T. Nagar', 501),
            cls(602, 'Blood-stained knife', 'Goripalayam', 502)
        ]
