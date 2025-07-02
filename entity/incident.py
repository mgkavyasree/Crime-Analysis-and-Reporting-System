class Incident:
    def __init__(self, incidentid=None, incidenttype=None, incidentdate=None, location=None,
                 description=None, status=None, agencyid=None):
        self.__incidentid = incidentid
        self.__incidenttype = incidenttype
        self.__incidentdate = incidentdate
        self.__location = location
        self.__description = description
        self.__status = status
        self.__agencyid = agencyid

    def get_incidentid(self):
        return self.__incidentid

    def set_incidentid(self, incidentid):
        self.__incidentid = incidentid

    def get_incidenttype(self):
        return self.__incidenttype

    def set_incidenttype(self, incidenttype):
        self.__incidenttype = incidenttype

    def get_incidentdate(self):
        return self.__incidentdate

    def set_incidentdate(self, incidentdate):
        self.__incidentdate = incidentdate

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_agencyid(self):
        return self.__agencyid

    def set_agencyid(self, agencyid):
        self.__agencyid = agencyid

    @classmethod
    def sample_data(cls):
        return [
            cls(501, 'Theft', '2024-05-12', 'T. Nagar, Chennai', 'Stolen motorcycle', 'Open', 101),
            cls(502, 'Assault', '2024-06-01', 'Goripalayam, Madurai', 'Street fight', 'Closed', 102)
        ]
