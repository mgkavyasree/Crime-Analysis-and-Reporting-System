class Victim:
    def __init__(self, victimid=None, firstname=None, lastname=None, dateofbirth=None, gender=None, contactinfo=None):
        self.victimid = victimid
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.contactinfo = contactinfo

    def get_victimid(self):
        return self.victimid

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_dateofbirth(self):
        return self.dateofbirth

    def get_gender(self):
        return self.gender

    def get_contactinfo(self):
        return self.contactinfo

    def set_victimid(self, victimid):
        self.victimid = victimid

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_dateofbirth(self, dateofbirth):
        self.dateofbirth = dateofbirth

    def set_gender(self, gender):
        self.gender = gender

    def set_contactinfo(self, contactinfo):
        self.contactinfo = contactinfo

    @classmethod
    def sample_data(cls):
        return [
            cls(301, 'Sundar', 'Rajan', '1985-06-15', 'Male', 'sundar.rajan@gmail.com'),
            cls(302, 'Latha', 'Nair', '1992-03-12', 'Female', 'latha.nair@gmail.com')
        ]
