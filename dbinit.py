import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
     """ 
CREATE TABLE IF NOT EXISTS attendances(
    id SERIAL PRIMARY KEY,
    upper_limit_percent INTEGER CHECK(upper_limit_percent<=100 AND upper_limit_percent>=0),
    attendance_hour1 INTEGER DEFAULT(0),
    attendance_hour2 INTEGER DEFAULT(0),
    attendance_hour3 INTEGER DEFAULT(0),
    attendance_hour4 INTEGER DEFAULT(0),
    attendance_hour5 INTEGER DEFAULT(0),
    attendance_hour6 INTEGER DEFAULT(0),
    attendance_hour7 INTEGER DEFAULT(0),
    attendance_hour8 INTEGER DEFAULT(0),
    attendance_hour9 INTEGER DEFAULT(0),
    attendance_hour10 INTEGER DEFAULT(0),
    attendance_hour11 INTEGER DEFAULT(0),
    attendance_hour12 INTEGER DEFAULT(0),
    attendance_hour13 INTEGER DEFAULT(0),
    attendance_hour14 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
"""
,
"""
CREATE TABLE IF NOT EXISTS homeworks(
    id SERIAL PRIMARY KEY,
    number_of_homework INTEGER ,
    homework_weight INTEGER CHECK(homework_weight<=100 AND homework_weight>=0),
    homework_score1 INTEGER DEFAULT(0),
    homework_score2 INTEGER DEFAULT(0),
    homework_score3 INTEGER DEFAULT(0),
    homework_score4 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
"""
,
"""
CREATE TABLE IF NOT EXISTS midterms(
    id SERIAL PRIMARY KEY,
    number_of_midterm INTEGER ,
    midterm_weight INTEGER CHECK(midterm_weight<=100 AND midterm_weight>=0),
    midterm_score1 INTEGER DEFAULT(0),
    midterm_score2 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
"""
,
"""
CREATE TABLE IF NOT EXISTS projects(
    id SERIAL PRIMARY KEY,
    number_of_project INTEGER ,
    project_weight INTEGER CHECK(project_weight<=100 AND project_weight>=0)  ,
    project_score1 INTEGER DEFAULT(0),
    project_score2 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
"""
,
"""
CREATE TABLE IF NOT EXISTS vf_conditions(
    id SERIAL PRIMARY KEY,
    attendance INTEGER,
    midterm INTEGER,
    homework INTEGER,
    project INTEGER
);
"""
,
"""
CREATE TABLE IF NOT EXISTS courses(
    id SERIAL PRIMARY KEY,
    department VARCHAR(50),
    course_name VARCHAR(100) ,
    course_description VARCHAR(100) ,
    lecturer_name VARCHAR(100) ,
    vf_condition INTEGER
);
"""
,
"""
CREATE TABLE IF NOT EXISTS user_course(
    user_course_id INTEGER,
    course_no INTEGER,
    PRIMARY KEY(user_course_id,course_no)
);
"""
,
"""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL ,
    mail VARCHAR(100) ,
    pass VARCHAR(50) NOT NULL
);
"""
,
"""
ALTER TABLE attendances ADD CONSTRAINT num1 FOREIGN KEY(id) REFERENCES courses(id);
"""
,
"""
ALTER TABLE homeworks ADD CONSTRAINT num2 FOREIGN KEY(id) REFERENCES courses(id);
"""
,
"""
ALTER TABLE midterms ADD CONSTRAINT num3 FOREIGN KEY(id) REFERENCES courses(id);
"""
,
"""
ALTER TABLE projects ADD CONSTRAINT num4 FOREIGN KEY(id) REFERENCES courses(id);
"""
,
"""
ALTER TABLE vf_conditions ADD CONSTRAINT num5 FOREIGN KEY(id) REFERENCES courses(id);
"""
,
"""
ALTER TABLE user_course ADD CONSTRAINT num10 FOREIGN KEY(user_course_id) REFERENCES  users(id);
"""
,
"""
ALTER TABLE user_course ADD CONSTRAINT num11 FOREIGN KEY(course_no) REFERENCES courses(id);
"""
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
