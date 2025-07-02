class Agency:
    def __init__(self, agencyid=None, agencyname=None, jurisdiction=None, contactinfo=None):
        self.agencyid = agencyid
        self.agencyname = agencyname
        self.jurisdiction = jurisdiction
        self.contactinfo = contactinfo

    def get_agencyid(self):
        return self.agencyid

    def get_agencyname(self):
        return self.agencyname

    def get_jurisdiction(self):
        return self.jurisdiction

    def get_contactinfo(self):
        return self.contactinfo

    def set_agencyid(self, agencyid):
        self.agencyid = agencyid

    def set_agencyname(self, agencyname):
        self.agencyname = agencyname

    def set_jurisdiction(self, jurisdiction):
        self.jurisdiction = jurisdiction

    def set_contactinfo(self, contactinfo):
        self.contactinfo = contactinfo


    @classmethod
    def sample_data(cls):
        return [
            cls(101, 'Chennai City Police', 'Chennai', '044-100'),
            cls(102, 'Madurai Police', 'Madurai', '0452-100')
        ]
