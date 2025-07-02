class Officer:
    def __init__(self, officerid=None, firstname=None, lastname=None, badgenumber=None, rank=None, contactinfo=None, agencyid=None):
        self.officerid = officerid
        self.firstname = firstname
        self.lastname = lastname
        self.badgenumber = badgenumber
        self.rank = rank
        self.contactinfo = contactinfo
        self.agencyid = agencyid

    def get_officerid(self):
        return self.officerid

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_badgenumber(self):
        return self.badgenumber

    def get_rank(self):
        return self.rank

    def get_contactinfo(self):
        return self.contactinfo

    def get_agencyid(self):
        return self.agencyid

    def set_officerid(self, officerid):
        self.officerid = officerid

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_badgenumber(self, badgenumber):
        self.badgenumber = badgenumber

    def set_rank(self, rank):
        self.rank = rank

    def set_contactinfo(self, contactinfo):
        self.contactinfo = contactinfo

    def set_agencyid(self, agencyid):
        self.agencyid = agencyid

    @classmethod
    def sample_data(cls):
        return [
            cls(201, 'Rajesh', 'Kumar', 'TN1001', 'Inspector', 'rajesh.k@tnpolice.gov.in', 101),
            cls(202, 'Priya', 'Ravi', 'TN1002', 'Sub Inspector', 'priya.r@tnpolice.gov.in', 102)
        ]
