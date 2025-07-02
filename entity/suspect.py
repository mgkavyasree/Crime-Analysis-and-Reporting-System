class Suspect:
    def __init__(self, suspectid=None, firstname=None, lastname=None, dateofbirth=None, gender=None, contactinfo=None):
        self.suspectid = suspectid
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.contactinfo = contactinfo

    def get_suspectid(self):
        return self.suspectid

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

    def set_suspectid(self, suspectid):
        self.suspectid = suspectid

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
            cls(401, 'Mohan', 'Das', '1980-02-14', 'Male', 'mohan.das@gmail.com'),
            cls(402, 'Kavitha', 'Sree', '1991-08-23', 'Female', 'kavitha.sree@gmail.com')
        ]
