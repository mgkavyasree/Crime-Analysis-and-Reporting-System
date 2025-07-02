import unittest
from dao.crimeserviceimpl import CrimeServiceImpl
from entity.incident import Incident
from exception.incidentnumbernotfoundexception import IncidentNumberNotFoundException

class IncidentServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = CrimeServiceImpl()
        cls.test_incident = Incident(
            None,
            "Test Robbery",
            "2025-07-30",
            "Chennai Central",
            "Test case incident",
            "Open",
            1
        )
        cls.service.create_incident(cls.test_incident)
        all_incidents = cls.service.search_incidents("Test Robbery")
        cls.valid_incident_id = all_incidents[-1].get_incidentid() if all_incidents else None

    def test_create_incident(self):
        new_inc = Incident(
            None,
            "Test Theft",
            "2025-08-01",
            "Madurai",
            "Test create incident function",
            "Open",
            1
        )
        result = self.service.create_incident(new_inc)
        self.assertTrue(result, "Incident should be created successfully.")

    def test_created_incident_attributes(self):
        results = self.service.search_incidents("Test Robbery")
        self.assertGreater(len(results), 0, "At least one incident should exist for the type.")
        inc = results[-1]
        self.assertEqual(inc.get_incidenttype(), "Test Robbery")
        self.assertEqual(inc.get_location(), "Chennai Central")
        self.assertEqual(inc.get_status(), "Open")

    def test_update_incident_status_valid(self):
        if self.valid_incident_id:
            result = self.service.update_incident_status("Closed", self.valid_incident_id)
            self.assertTrue(result, "Status should update successfully.")
        else:
            self.fail("Valid incident ID not found for testing.")

    def test_update_incident_status_invalid(self):
        with self.assertRaises(IncidentNumberNotFoundException):
            self.service.update_incident_status("Closed", 999999)

if __name__ == '__main__':
    unittest.main()
