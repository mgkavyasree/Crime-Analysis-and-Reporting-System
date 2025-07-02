-- Create database
drop database crime_db;
create database if not exists crime_db;
use crime_db;

-- Agencies
create table agencies (
    agencyid int primary key auto_increment,
    agencyname varchar(100) not null,
    jurisdiction varchar(100),
    contactinfo varchar(100)
);

-- Officers (1 agency → many officers)
create table officers (
    officerid int primary key auto_increment,
    firstname varchar(50),
    lastname varchar(50),
    badgenumber varchar(20),
    `rank` varchar(50),
    contactinfo varchar(100),
    agencyid int not null,
    foreign key (agencyid) references agencies(agencyid)
);

-- Victims
create table victims (
    victimid int primary key auto_increment,
    firstname varchar(50),
    lastname varchar(50),
    dateofbirth date,
    gender varchar(10),
    contactinfo varchar(100)
);

-- Suspects
create table suspects (
    suspectid int primary key auto_increment,
    firstname varchar(50),
    lastname varchar(50),
    dateofbirth date,
    gender varchar(10),
    contactinfo varchar(100)
);

-- Incidents (1 agency → many incidents)
create table incidents (
    incidentid int primary key auto_increment,
    incidenttype varchar(50),
    incidentdate date,
    location varchar(100),
    description text,
    status varchar(50),
    agencyid int not null,
    foreign key (agencyid) references agencies(agencyid)
);

-- Incident-Victim (many-to-many)
create table incident_victims (
    incidentid int,
    victimid int,
    primary key (incidentid, victimid),
    foreign key (incidentid) references incidents(incidentid) on delete cascade,
    foreign key (victimid) references victims(victimid) on delete cascade
);

-- Incident-Suspect (many-to-many)
create table incident_suspects (
    incidentid int,
    suspectid int,
    primary key (incidentid, suspectid),
    foreign key (incidentid) references incidents(incidentid) on delete cascade,
    foreign key (suspectid) references suspects(suspectid) on delete cascade
);

-- Evidence (many per incident)
create table evidence (
    evidenceid int primary key auto_increment,
    description text,
    locationfound varchar(100),
    incidentid int not null,
    foreign key (incidentid) references incidents(incidentid)
);

-- Reports (1 officer per report, many reports per incident)
create table reports (
    reportid int primary key auto_increment,
    incidentid int not null,
    reportingofficer int not null,
    reportdate date,
    reportdetails text,
    status varchar(50),
    foreign key (incidentid) references incidents(incidentid),
    foreign key (reportingofficer) references officers(officerid)
);
