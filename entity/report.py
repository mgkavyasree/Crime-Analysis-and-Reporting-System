class Report:
    def __init__(self, reportid, incidentid, reportingofficer, reportdate, reportdetails, status, officer_name=None):
        self.reportid = reportid
        self.incidentid = incidentid
        self.reportingofficer = reportingofficer
        self.reportdate = reportdate
        self.reportdetails = reportdetails
        self.status = status
        self.officer_name = officer_name

    def get_reportid(self):
        return self.reportid
    def get_incidentid(self):
        return self.incidentid
    def get_reportingofficer(self):
        return self.reportingofficer
    def get_reportdate(self):
        return self.reportdate
    def get_reportdetails(self):
        return self.reportdetails
    def get_status(self):
        return self.status
    def get_officer_name(self):
        return self.officer_name

    @classmethod
    def sample_data(cls):
        return [
            cls(701, 501, 201, '2024-05-13', 'Initial complaint registered', 'Filed'),
            cls(702, 502, 202, '2024-06-02', 'Case closed after resolution', 'Closed')
        ]
