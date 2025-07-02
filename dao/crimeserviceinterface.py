from abc import ABC, abstractmethod
from typing import List
from entity.incident import Incident
from entity.case import Case
from entity.report import Report
from entity.victim import Victim
from entity.suspect import Suspect
from entity.evidence import Evidence
from entity.officer import Officer
from entity.agency import Agency

class CrimeServiceInterface(ABC):

    @abstractmethod
    def create_incident(self, inc: Incident) -> bool: pass

    @abstractmethod
    def update_incident_status(self, status: str, incident_id: int) -> bool: pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> List[Incident]: pass

    @abstractmethod
    def search_incidents(self, incident_type: str) -> List[Incident]: pass

    @abstractmethod
    def get_incidents_by_month(self, month: int, year: int) -> List[Incident]: pass

    @abstractmethod
    def get_incidents_by_year(self, year: int) -> List[Incident]: pass

    @abstractmethod
    def view_all_incidents(self) -> List[Incident]: pass

    @abstractmethod
    def generate_incident_report(self, inc: Incident) -> Report: pass

    @abstractmethod
    def view_all_reports(self) -> List[Report]: pass

    @abstractmethod
    def create_case(self, description: str, incidents: List[Incident]) -> Case: pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> Case: pass

    @abstractmethod
    def update_case_details(self, case: Case) -> bool: pass

    @abstractmethod
    def get_all_cases(self) -> List[Case]: pass

    @abstractmethod
    def add_victim(self, vic: Victim) -> bool: pass

    @abstractmethod
    def view_all_victims(self) -> List[Victim]: pass

    @abstractmethod
    def add_suspect(self, sus: Suspect) -> bool: pass

    @abstractmethod
    def view_all_suspects(self) -> List[Suspect]: pass

    @abstractmethod
    def add_officer(self, officer: Officer) -> bool: pass

    @abstractmethod
    def view_all_officers(self) -> List[Officer]: pass

    @abstractmethod
    def add_agency(self, agency: Agency) -> bool: pass

    @abstractmethod
    def view_all_agencies(self) -> List[Agency]: pass

    @abstractmethod
    def add_evidence(self, evidence: Evidence) -> bool: pass

    @abstractmethod
    def view_all_evidence(self) -> List[Evidence]: pass
