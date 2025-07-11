# Crime Analysis and Reporting System

## Project Overview

The Crime Analysis and Reporting System is designed to streamline and digitize law enforcement data workflows. It supports a wide range of operations including:

* **Incident Reporting and Tracking**: Log and monitor all criminal incidents, including type, location, date, and status.
* **Case Management**: Group multiple related incidents into cases, manage case descriptions, and track their progress.
* **Suspect and Victim Management**: Store and associate individuals involved in incidents, with contact and demographic details.
* **Evidence Handling**: Maintain detailed records of evidence collected for each incident.
* **Officer and Agency Records**: Manage personnel and agency details, including ranks and assignments.
* **Search and Filter Operations**: Retrieve data by type, date, and keyword to support investigations.
* **Report Generation**: Generate detailed reports for specific incidents, authored by designated officers.

## Project Directory Structure

```
Crime-Analysis-and-Reporting-System/
├── entity/             # Domain model classes (Incident, Case, Victim, etc.)
├── service/            # Service interface and implementation (CRUD logic)
├── util/               # Utilities (e.g., DB connection, validation)
├── db.properties.py    # Database configuration settings
├── main.py             # Main module (entry point for CLI or UI)
├── README.md           # Project documentation
└── .git/               # Git metadata (if applicable)
```

## Key Features

### Incident Management

* Create new incident records with type, date, location, and description
* Update the status of incidents (e.g., open, under investigation, closed)
* Search incidents by type, or by specific date ranges
* Retrieve incidents filtered by month or year for statistical analysis

### Case Management

* Create new cases and associate multiple incidents to each case
* Update case descriptions to reflect new findings or changes
* View all existing cases or search by keyword in descriptions

### Report Management

* Generate formal reports for incidents, authored by specific officers
* View all existing reports along with officer details and status

### Victim and Suspect Tracking

* Add victim and suspect records with name, DOB, gender, and contact info
* Link victims and suspects to specific incidents
* Retrieve all victims or suspects involved in a particular incident

### Evidence Handling

* Add evidence entries with description and location found
* Associate each evidence item with an incident
* View or delete evidence as needed

### Officer and Agency Records

* Add new officers including badge number, rank, and agency affiliation
* Add new agencies with jurisdiction and contact details
* View all officers and agencies registered in the system

## Database Schema Design

The system uses a MySQL relational database schema with normalized tables and defined relationships.

### Tables

* `agencies` – Stores agency names, jurisdictions, and contact information
* `officers` – Contains officer details, linked to an agency
* `victims` and `suspects` – Store individuals' personal and contact data
* `incidents` – Core entity for criminal events
* `evidence` – Items collected in relation to incidents
* `reports` – Reports created by officers for incidents
* `cases` – Logical groupings of one or more incidents
* `incident_victims` and `incident_suspects` – Junction tables managing many-to-many relationships

### Relationships

* One **agency** can be associated with multiple **officers** and **incidents**
* One **incident** can have multiple **victims**, **suspects**, **evidence items**, and **reports**
* One **case** can include multiple **incidents**
* One **report** is authored by an **officer** for a specific **incident**

## Validation Rules

* **Required Fields**: Fields like first name, last name, contact info, incident type, and status must not be empty.
* **Contact Info**: Must be a valid email format or a 10-digit mobile number.
* **Date Fields**: Dates must not be set in the future (e.g., incident date, date of birth).
* **Referential Integrity**: Incident and case IDs used in associations must exist in the corresponding tables.

