CREATE OR REPLACE TABLE clases (
id INT PRIMARY KEY,
name VARCHAR(255),
class_time DATETIME,
Docente VARCHAR(255)
);
CREATE OR REPLACE TABLE registrants (
id INT PRIMARY KEY,
email_atendee VARCHAR(255),
registrant_date DATETIME,
FOREIGN KEY (class_id) REFERENCES clases(id)
);
CREATE OR REPLACE TABLE attendee (
id INT PRIMARY KEY,
join_time DATETIME,
leave_time DATETIME,
FOREIGN KEY (email_atendee) REFERENCES registrants
(email_atendee)
);
CREATE TABLE tabla_sumarizada (
    id_clase INT,
    class_name VARCHAR(255),
    professor_name VARCHAR(255),
    fecha_clase DATE,
    email VARCHAR(255),
    registrant_date DATETIME,
    attendee_join_date DATETIME,
    attendee_leave_date DATETIME,
    attende_seconds_duration INT
);