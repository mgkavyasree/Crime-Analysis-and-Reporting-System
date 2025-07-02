import re
from datetime import datetime
from typing import List
from entity.incident import Incident
from entity.report import Report
from entity.case import Case
from entity.evidence import Evidence
from entity.victim import Victim
from entity.suspect import Suspect
from entity.officer import Officer
from entity.agency import Agency
from util.dbconnutil import DBConnUtil

class ValidationException(Exception):
    pass

def validate_not_empty(value, field_name):
    if not value or str(value).strip() == "":
        raise ValidationException(f"{field_name} cannot be empty.")

def validate_contact_info(info):
    if "@" in info:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", info):
            raise ValidationException("Invalid email format.")
    elif info.isdigit():
        if not re.match(r"^\d{10}$", info):
            raise ValidationException("Invalid mobile number format.")
    else:
        raise ValidationException("Contact info must be a valid email or mobile number.")

def validate_date_not_future(date_val, field_name):
    if isinstance(date_val, str):
        date_val = datetime.strptime(date_val, "%Y-%m-%d")
    if date_val > datetime.now():
        raise ValidationException(f"{field_name} cannot be in the future.")

class CrimeServiceImpl:

    def __init__(self):
        self.connection = DBConnUtil.getconnection()

    def create_incident(self, inc: Incident) -> bool:
        try:
            validate_not_empty(inc.get_incidenttype(), "Incident Type")
            validate_not_empty(inc.get_location(), "Location")
            validate_not_empty(inc.get_description(), "Description")
            validate_not_empty(inc.get_status(), "Status")
            validate_not_empty(inc.get_agencyid(), "Agency ID")
            validate_date_not_future(inc.get_incidentdate(), "Incident Date")

            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO incidents (incidenttype, incidentdate, location, description, status, agencyid)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                inc.get_incidenttype(), inc.get_incidentdate(), inc.get_location(),
                inc.get_description(), inc.get_status(), inc.get_agencyid()
            ))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Create incident failed:", e)
            return False

    def update_incident_status(self, status: str, incidentid: int) -> bool:
        try:
            validate_not_empty(status, "Status")
            validate_not_empty(incidentid, "Incident ID")

            cursor = self.connection.cursor()
            cursor.execute("UPDATE incidents SET status=%s WHERE incidentid=%s", (status, incidentid))
            self.connection.commit()
            return cursor.rowcount > 0
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Update incident status failed:", e)
            return False

    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> List[Incident]:
        try:
            validate_not_empty(start_date, "Start Date")
            validate_not_empty(end_date, "End Date")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM incidents WHERE incidentdate BETWEEN %s AND %s", (start_date, end_date))
            return [Incident(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get incidents in range failed:", e)
            return []

    def search_incidents(self, incidenttype: str) -> List[Incident]:
        try:
            validate_not_empty(incidenttype, "Incident Type")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM incidents WHERE incidenttype=%s", (incidenttype,))
            return [Incident(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Search incidents failed:", e)
            return []

    def delete_incident(self, incidentid: int) -> bool:
        try:
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM incidents WHERE incidentid=%s", (incidentid,))
            self.connection.commit()
            return cursor.rowcount > 0
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Delete incident failed:", e)
            return False

    def generate_incident_report(self, inc: Incident) -> Report:
        try:
            validate_not_empty(inc.get_incidentid(), "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("""SELECT r.reportid, r.incidentid, r.reportingofficer, r.reportdate,
                                     r.reportdetails, r.status, o.firstname, o.lastname
                              FROM reports r
                              JOIN officers o ON r.reportingofficer = o.officerid
                              WHERE r.incidentid = %s""", (inc.get_incidentid(),))
            row = cursor.fetchone()
            if row:
                report = Report(row[0], row[1], row[2], row[3], row[4], row[5])
                report.officer_name = f"{row[6]} {row[7]}"
                return report
            return None
        except ValidationException as ve:
            print("Validation error:", ve)
            return None
        except Exception as e:
            print("Generate incident report failed:", e)
            return None

    def create_case(self, casedescription: str, incidents: List[Incident]) -> Case:
        try:
            validate_not_empty(casedescription, "Case Description")
            if not incidents:
                raise ValidationException("Case must include at least one incident.")

            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO cases (casedescription) VALUES (%s)", (casedescription,))
            case_id = cursor.lastrowid
            for inc in incidents:
                validate_not_empty(inc.get_incidentid(), "Incident ID")
                cursor.execute("SELECT 1 FROM incidents WHERE incidentid = %s", (inc.get_incidentid(),))
                if cursor.fetchone() is None:
                    raise ValidationException(f"Incident ID {inc.get_incidentid()} does not exist.")
                cursor.execute("INSERT INTO case_incident (caseid, incidentid) VALUES (%s, %s)",
                               (case_id, inc.get_incidentid()))
            self.connection.commit()
            return Case(case_id, casedescription, incidents)
        except ValidationException as ve:
            print("Validation error:", ve)
            return None
        except Exception as e:
            print("Create case failed:", e)
            return None

    def get_case_details(self, case_id: int) -> Case:
        try:
            validate_not_empty(case_id, "Case ID")
            cursor = self.connection.cursor()
            cursor.execute("SELECT casedescription FROM cases WHERE caseid=%s", (case_id,))
            desc_row = cursor.fetchone()
            if not desc_row:
                return None
            description = desc_row[0]
            cursor.execute("SELECT incidentid FROM case_incident WHERE caseid=%s", (case_id,))
            incidents = [Incident(incidentid=r[0]) for r in cursor.fetchall()]
            return Case(case_id, description, incidents)
        except ValidationException as ve:
            print("Validation error:", ve)
            return None
        except Exception as e:
            print("Get case failed:", e)
            return None

    def update_case_details(self, case: Case) -> bool:
        try:
            validate_not_empty(case.get_caseid(), "Case ID")
            validate_not_empty(case.get_casedescription(), "Case Description")

            cursor = self.connection.cursor()
            cursor.execute("UPDATE cases SET casedescription=%s WHERE caseid=%s",
                           (case.get_casedescription(), case.get_caseid()))
            self.connection.commit()
            return cursor.rowcount > 0
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Update case failed:", e)
            return False

    def get_all_cases(self) -> List[Case]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT caseid, casedescription FROM cases")
            return [Case(row[0], row[1], []) for row in cursor.fetchall()]
        except Exception as e:
            print("Get all cases failed:", e)
            return []

    def delete_case(self, caseid: int) -> bool:
        try:
            validate_not_empty(caseid, "Case ID")
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM cases WHERE caseid=%s", (caseid,))
            self.connection.commit()
            return cursor.rowcount > 0
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Delete case failed:", e)
            return False

    def search_case_by_description(self, keyword: str) -> List[Case]:
        try:
            validate_not_empty(keyword, "Search Keyword")
            cursor = self.connection.cursor()
            cursor.execute("SELECT caseid, casedescription FROM cases WHERE casedescription LIKE %s",
                           ('%' + keyword + '%',))
            return [Case(row[0], row[1], []) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Search case failed:", e)
            return []

    def add_evidence(self, evidence: Evidence) -> bool:
        try:
            validate_not_empty(evidence.get_description(), "Evidence Description")
            validate_not_empty(evidence.get_locationfound(), "Location Found")
            validate_not_empty(evidence.get_incidentid(), "Incident ID")

            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO evidence (description, locationfound, incidentid) VALUES (%s, %s, %s)",
                           (evidence.get_description(), evidence.get_locationfound(), evidence.get_incidentid()))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add evidence failed:", e)
            return False

    def get_evidence_by_incident(self, incidentid: int) -> List[Evidence]:
        try:
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM evidence WHERE incidentid=%s", (incidentid,))
            return [Evidence(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get evidence failed:", e)
            return []

    def delete_evidence(self, evidenceid: int) -> bool:
        try:
            validate_not_empty(evidenceid, "Evidence ID")
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM evidence WHERE evidenceid=%s", (evidenceid,))
            self.connection.commit()
            return cursor.rowcount > 0
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Delete evidence failed:", e)
            return False

    def add_victim_to_incident(self, victimid: int, incidentid: int) -> bool:
        try:
            validate_not_empty(victimid, "Victim ID")
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO incident_victims (incidentid, victimid) VALUES (%s, %s)",
                           (incidentid, victimid))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add victim failed:", e)
            return False

    def add_suspect_to_incident(self, suspectid: int, incidentid: int) -> bool:
        try:
            validate_not_empty(suspectid, "Suspect ID")
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO incident_suspects (incidentid, suspectid) VALUES (%s, %s)",
                           (incidentid, suspectid))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add suspect failed:", e)
            return False

    def get_victims_by_incident(self, incidentid: int) -> List[Victim]:
        try:
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT v.* FROM victims v
                JOIN incident_victims iv ON v.victimid = iv.victimid
                WHERE iv.incidentid = %s
            """, (incidentid,))
            return [Victim(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get victims failed:", e)
            return []

    def get_suspects_by_incident(self, incidentid: int) -> List[Suspect]:
        try:
            validate_not_empty(incidentid, "Incident ID")
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT s.* FROM suspects s
                JOIN incident_suspects isus ON s.suspectid = isus.suspectid
                WHERE isus.incidentid = %s
            """, (incidentid,))
            return [Suspect(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get suspects failed:", e)
            return []

    def view_all_incidents(self) -> List[Incident]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM incidents")
            return [Incident(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all incidents failed:", e)
            return []

    def view_all_reports(self) -> List[Report]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT r.reportid, r.incidentid, r.reportingofficer, r.reportdate,
                       r.reportdetails, r.status, o.firstname, o.lastname
                FROM reports r
                JOIN officers o ON r.reportingofficer = o.officerid
            """)
            reports = []
            for row in cursor.fetchall():
                report = Report(row[0], row[1], row[2], row[3], row[4], row[5])
                report.officer_name = f"{row[6]} {row[7]}"
                reports.append(report)
            return reports
        except Exception as e:
            print("View all reports failed:", e)
            return []

    def view_all_victims(self) -> List[Victim]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM victims")
            return [Victim(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all victims failed:", e)
            return []

    def view_all_suspects(self) -> List[Suspect]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM suspects")
            return [Suspect(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all suspects failed:", e)
            return []

    def view_all_officers(self) -> List[Officer]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM officers")
            return [Officer(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all officers failed:", e)
            return []

    def view_all_agencies(self) -> List[Agency]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM agencies")
            return [Agency(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all agencies failed:", e)
            return []

    def view_all_evidence(self) -> List[Evidence]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM evidence")
            return [Evidence(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("View all evidence failed:", e)
            return []

    def get_incidents_by_month(self, month: int) -> List[Incident]:
        try:
            if not (1 <= month <= 12):
                raise ValidationException("Month must be between 1 and 12.")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM incidents WHERE MONTH(incidentdate) = %s", (month,))
            return [Incident(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get incidents by month failed:", e)
            return []

    def get_incidents_by_year(self, year: int) -> List[Incident]:
        try:
            if year < 1900 or year > datetime.now().year:
                raise ValidationException("Invalid year provided.")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM incidents WHERE YEAR(incidentdate) = %s", (year,))
            return [Incident(*row) for row in cursor.fetchall()]
        except ValidationException as ve:
            print("Validation error:", ve)
            return []
        except Exception as e:
            print("Get incidents by year failed:", e)
            return []

    def add_victim(self, victim: Victim) -> bool:
        try:
            validate_not_empty(victim.get_firstname(), "First Name")
            validate_not_empty(victim.get_lastname(), "Last Name")
            validate_not_empty(victim.get_dateofbirth(), "Date of Birth")
            validate_not_empty(victim.get_gender(), "Gender")
            validate_contact_info(victim.get_contactinfo())

            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO victims (firstname, lastname, dateofbirth, gender, contactinfo)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                victim.get_firstname(),
                victim.get_lastname(),
                victim.get_dateofbirth(),
                victim.get_gender(),
                victim.get_contactinfo()
            ))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add victim failed:", e)
            return False

    def add_suspect(self, suspect: Suspect) -> bool:
        try:
            validate_not_empty(suspect.get_firstname(), "First Name")
            validate_not_empty(suspect.get_lastname(), "Last Name")
            validate_not_empty(suspect.get_dateofbirth(), "Date of Birth")
            validate_not_empty(suspect.get_gender(), "Gender")
            validate_contact_info(suspect.get_contactinfo())

            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO suspects (firstname, lastname, dateofbirth, gender, contactinfo)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                suspect.get_firstname(),
                suspect.get_lastname(),
                suspect.get_dateofbirth(),
                suspect.get_gender(),
                suspect.get_contactinfo()
            ))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add suspect failed:", e)
            return False

    def add_officer(self, officer: Officer) -> bool:
        try:
            validate_not_empty(officer.get_firstname(), "First Name")
            validate_not_empty(officer.get_lastname(), "Last Name")
            validate_not_empty(officer.get_badgenumber(), "Badge Number")
            validate_not_empty(officer.get_rank(), "Rank")
            validate_contact_info(officer.get_contactinfo())
            validate_not_empty(officer.get_agencyid(), "Agency ID")
            with self.connection.cursor() as cursor:
                cursor.execute("""
                               INSERT INTO officers (firstname, lastname, badgenumber, `rank`, contactinfo, agencyid)
                               VALUES (%s, %s, %s, %s, %s, %s)
                               """, (
                                   officer.get_firstname(),
                                   officer.get_lastname(),
                                   officer.get_badgenumber(),
                                   officer.get_rank(),
                                   officer.get_contactinfo(),
                                   officer.get_agencyid()
                               ))
                self.connection.commit()
                return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add officer failed:", e)
            return False

    def add_agency(self, agency: Agency) -> bool:
        try:
            validate_not_empty(agency.get_agencyname(), "Agency Name")
            validate_not_empty(agency.get_jurisdiction(), "Jurisdiction")
            validate_contact_info(agency.get_contactinfo())

            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO agencies (agencyname, jurisdiction, contactinfo)
                VALUES (%s, %s, %s)
            """, (
                agency.get_agencyname(),
                agency.get_jurisdiction(),
                agency.get_contactinfo()
            ))
            self.connection.commit()
            return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Add agency failed:", e)
            return False

    def update_incident_status(self, status: str, incidentid: int) -> bool:
        try:
            validate_not_empty(status, "Status")
            if not isinstance(incidentid, int) or incidentid <= 0:
                raise ValidationException("Incident ID must be a positive integer.")
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT incidentid FROM incidents WHERE incidentid = %s", (incidentid,))
                if not cursor.fetchone():
                    print(f"No incident found with ID: {incidentid}")
                    return False
                cursor.execute(
                    "UPDATE incidents SET status = %s WHERE incidentid = %s",
                    (status, incidentid)
                )
                self.connection.commit()
                return True
        except ValidationException as ve:
            print("Validation error:", ve)
            return False
        except Exception as e:
            print("Update incident status failed:", e)
            return False

