from dao.crimeserviceimpl import CrimeServiceImpl
from entity.incident import Incident
from entity.case import Case
from entity.victim import Victim
from entity.suspect import Suspect
from entity.evidence import Evidence
from entity.officer import Officer
from entity.agency import Agency
from entity.report import Report

def main():
    service = CrimeServiceImpl()

    while True:
        print("\n===== Crime Analysis and Reporting System (C.A.R.S.) =====")
        print("Select a category:")
        print("1. Incident Management")
        print("2. Victim & Suspect Management")
        print("3. Evidence Management")
        print("4. Officer & Agency Management")
        print("5. Case Management")
        print("6. Reports")
        print("7. Exit")

        category = input("Enter your choice (1-7): ").strip()

        try:
            if category == '1':
                while True:
                    print("\n--- Incident Management ---")
                    print(" 1. Add Incident")
                    print(" 2. Update Incident Status")
                    print(" 3. Delete Incident")
                    print(" 4. View All Incidents")
                    print(" 5. Search Incidents by Type")
                    print(" 6. List Incidents by Date Range")
                    print(" 7. List Incidents by Month")
                    print(" 8. List Incidents by Year")
                    print(" 9. Generate Report for Incident")
                    print("10. Back to Main Menu")

                    choice = input("Select an option: ")

                    if choice == '1':
                        inc = Incident(
                            None,
                            input("Incident type: "),
                            input("Incident date (YYYY-MM-DD): "),
                            input("Location: "),
                            input("Description: "),
                            input("Status: "),
                            int(input("Agency ID: "))
                        )
                        print("Incident added." if service.create_incident(inc) else "Failed to add incident.")


                    elif choice == '2':
                        incidentid = int(input("Incident ID: "))
                        status = input("New status: ")
                        print("Status updated." if service.update_incident_status(status, incidentid) else "Failed to update.")

                    elif choice == '3':
                        incidentid = int(input("Incident ID to delete: "))
                        print("Incident deleted." if service.delete_incident(incidentid) else "Failed to delete.")

                    elif choice == '4':
                        for i in service.view_all_incidents():
                            print(f"[{i.get_incidentid()}] {i.get_incidenttype()} | {i.get_incidentdate()} | {i.get_status()}")

                    elif choice == '5':
                        t = input("Incident type: ")
                        for i in service.search_incidents(t):
                            print(f"[{i.get_incidentid()}] {i.get_incidenttype()} | {i.get_incidentdate()}")

                    elif choice == '6':
                        start = input("Start date (YYYY-MM-DD): ")
                        end = input("End date (YYYY-MM-DD): ")
                        for i in service.get_incidents_in_date_range(start, end):
                            print(f"[{i.get_incidentid()}] {i.get_incidenttype()} | {i.get_incidentdate()} | {i.get_status()}")

                    elif choice == '7':
                        month = int(input("Month (1-12): "))
                        for i in service.get_incidents_by_month(month):
                            print(f"[{i.get_incidentid()}] {i.get_incidenttype()} | {i.get_incidentdate()}")

                    elif choice == '8':
                        year = int(input("Year (e.g., 2023): "))
                        for i in service.get_incidents_by_year(year):
                            print(f"[{i.get_incidentid()}] {i.get_incidenttype()} | {i.get_incidentdate()}")

                    elif choice == '9':
                        iid = int(input("Incident ID: "))
                        inc = Incident()
                        inc.set_incidentid(iid)
                        r = service.generate_incident_report(inc)
                        if r:
                            print(f"Report ID: {r.get_reportid()} | Officer: {r.officer_name} | Date: {r.get_reportdate()}")
                            print(f"Details: {r.get_reportdetails()} | Status: {r.get_status()}")
                        else:
                            print("No report found.")

                    elif choice == '10':
                        break

            elif category == '2':
                while True:
                    print("\n--- Victim & Suspect Management ---")
                    print(" 1. Add Victim")
                    print(" 2. Add Suspect")
                    print(" 3. View All Victims")
                    print(" 4. View All Suspects")
                    print(" 5. Add Victim to Incident")
                    print(" 6. Add Suspect to Incident")
                    print(" 7. View Victims by Incident")
                    print(" 8. View Suspects by Incident")
                    print(" 9. Back to Main Menu")

                    choice = input("Select an option: ")

                    if choice == '1':
                        v = Victim(None,
                                   input("First name: "),
                                   input("Last name: "),
                                   input("DOB (YYYY-MM-DD): "),
                                   input("Gender: "),
                                   input("Contact info: "))
                        print("Victim added." if service.add_victim(v) else "Failed.")

                    elif choice == '2':
                        s = Suspect(None,
                                    input("First name: "),
                                    input("Last name: "),
                                    input("DOB (YYYY-MM-DD): "),
                                    input("Gender: "),
                                    input("Contact info: "))
                        print("Suspect added." if service.add_suspect(s) else "Failed.")

                    elif choice == '3':
                        for v in service.view_all_victims():
                            print(f"[{v.get_victimid()}] {v.get_firstname()} {v.get_lastname()} | {v.get_contactinfo()}")

                    elif choice == '4':
                        for s in service.view_all_suspects():
                            print(f"[{s.get_suspectid()}] {s.get_firstname()} {s.get_lastname()} | {s.get_contactinfo()}")

                    elif choice == '5':
                        vid = int(input("Victim ID: "))
                        iid = int(input("Incident ID: "))
                        print("Added." if service.add_victim_to_incident(vid, iid) else "Failed.")

                    elif choice == '6':
                        sid = int(input("Suspect ID: "))
                        iid = int(input("Incident ID: "))
                        print("Added." if service.add_suspect_to_incident(sid, iid) else "Failed.")

                    elif choice == '7':
                        iid = int(input("Incident ID: "))
                        for v in service.get_victims_by_incident(iid):
                            print(f"[{v.get_victimid()}] {v.get_firstname()} {v.get_lastname()} | {v.get_contactinfo()}")

                    elif choice == '8':
                        iid = int(input("Incident ID: "))
                        for s in service.get_suspects_by_incident(iid):
                            print(f"[{s.get_suspectid()}] {s.get_firstname()} {s.get_lastname()} | {s.get_contactinfo()}")

                    elif choice == '9':
                        break

            elif category == '3':
                while True:
                    print("\n--- Evidence Management ---")
                    print(" 1. Add Evidence")
                    print(" 2. Delete Evidence")
                    print(" 3. View All Evidence")
                    print(" 4. Back to Main Menu")

                    choice = input("Select an option: ")

                    if choice == '1':
                        e = Evidence(None,
                                     input("Description: "),
                                     input("Location Found: "),
                                     int(input("Incident ID: ")))
                        print("Evidence added." if service.add_evidence(e) else "Failed.")

                    elif choice == '2':
                        eid = int(input("Evidence ID: "))
                        print("Deleted." if service.delete_evidence(eid) else "Failed.")

                    elif choice == '3':
                        for e in service.view_all_evidence():
                            print(f"[{e.get_evidenceid()}] {e.get_description()} | Found: {e.get_locationfound()}")

                    elif choice == '4':
                        break

            elif category == '4':
                while True:
                    print("\n--- Officer & Agency Management ---")
                    print(" 1. Add Officer")
                    print(" 2. Add Agency")
                    print(" 3. View All Officers")
                    print(" 4. View All Agencies")
                    print(" 5. Back to Main Menu")

                    choice = input("Select an option: ")

                    if choice == '1':
                        o = Officer(None,
                                    input("First name: "),
                                    input("Last name: "),
                                    input("Badge number: "),
                                    input("Rank: "),
                                    input("Contact info: "),
                                    int(input("Agency ID: ")))
                        print("Officer added." if service.add_officer(o) else "Failed.")

                    elif choice == '2':
                        a = Agency(None,
                                   input("Agency name: "),
                                   input("Jurisdiction: "),
                                   input("Contact info: "))
                        print("Agency added." if service.add_agency(a) else "Failed.")

                    elif choice == '3':
                        for o in service.view_all_officers():
                            print(f"[{o.get_officerid()}] {o.get_firstname()} {o.get_lastname()} | {o.get_rank()}")

                    elif choice == '4':
                        for a in service.view_all_agencies():
                            print(f"[{a.get_agencyid()}] {a.get_agencyname()} | {a.get_jurisdiction()}")

                    elif choice == '5':
                        break

            elif category == '5':
                while True:
                    print("\n--- Case Management ---")
                    print(" 1. Create Case with Incidents")
                    print(" 2. View Case Details")
                    print(" 3. Update Case Description")
                    print(" 4. View All Cases")
                    print(" 5. Delete Case")
                    print(" 6. Back to Main Menu")

                    choice = input("Select an option: ")

                    if choice == '1':
                        desc = input("Case description: ")
                        n = int(input("How many incidents to link? "))
                        incidents = []
                        for _ in range(n):
                            iid = int(input("Incident ID: "))
                            inc = Incident()
                            inc.set_incidentid(iid)
                            incidents.append(inc)
                        c = service.create_case(desc, incidents)
                        print(f"Case created with ID: {c.get_caseid()}" if c else "Failed to create case.")

                    elif choice == '2':
                        cid = int(input("Case ID: "))
                        c = service.get_case_details(cid)
                        if c:
                            print(f"Case {c.get_caseid()} - {c.get_casedescription()}")
                            for i in c.get_incidents():
                                print(f"Incident ID: {i.get_incidentid()}")
                        else:
                            print("Case not found.")

                    elif choice == '3':
                        cid = int(input("Case ID: "))
                        desc = input("New description: ")
                        print("Updated." if service.update_case_details(Case(cid, desc)) else "Failed.")

                    elif choice == '4':
                        for c in service.get_all_cases():
                            print(f"[{c.get_caseid()}] {c.get_casedescription()}")

                    elif choice == '5':
                        cid = int(input("Case ID to delete: "))
                        print("Deleted." if service.delete_case(cid) else "Failed.")

                    elif choice == '6':
                        break

            elif category == '6':
                print("\n--- Reports ---")
                reports = service.view_all_reports()
                if not reports:
                    print("No reports available.")
                for r in reports:
                    print(f"[{r.get_reportid()}] Incident: {r.get_incidentid()} | Officer: {r.officer_name} | Date: {r.get_reportdate()}")

            elif category == '7':
                print("Exiting system.")
                break

            else:
                print("Invalid selection. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
