import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
     """
    CREATE TABLE IF NOT EXISTS attendances(
    id INTEGER PRIMARY KEY ,
    upper_limit_percent INTEGER ,
    total_hour INTEGER ,
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
""",
"""
CREATE TABLE IF NOT EXISTS homeworks(
    id INTEGER PRIMARY KEY ,
    number_of_homework INTEGER ,
    homework_weight INTEGER ,
    homework_score1 INTEGER DEFAULT(0),
    homework_score2 INTEGER DEFAULT(0),
    homework_score3 INTEGER DEFAULT(0),
    homework_score4 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
""",
"""
CREATE TABLE IF NOT EXISTS midterms(
    id INTEGER PRIMARY KEY ,
    number_of_midterm INTEGER ,
    midterm_weight INTEGER ,
    midterm_score1 INTEGER DEFAULT(0),
    midterm_score2 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
""",
"""
CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY ,
    number_of_project INTEGER ,
    project_weight INTEGER ,
    project_score1 INTEGER DEFAULT(0),
    project_score2 INTEGER DEFAULT(0),
    is_important BOOLEAN
);
""",
"""
CREATE TABLE IF NOT EXISTS vf_conditions(
    id INTEGER PRIMARY KEY ,
    attendance INTEGER REFERENCES attendances(id),
    midterm INTEGER REFERENCES midterms(id),
    homework INTEGER REFERENCES homeworks(id),
    project INTEGER REFERENCES projects(id)
);
""",
"""
CREATE TABLE IF NOT EXISTS courses(
    id SERIAL PRIMARY KEY ,
    department VARCHAR(50) NOT NULL ,
    course_name VARCHAR(100) NOT NULL ,
    course_description VARCHAR(100) ,
    lecturer_name VARCHAR(100) ,
    VF_condition VARCHAR(10)
);
""",
"""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY ,
    username VARCHAR(50) NOT NULL ,
    full_name VARCHAR(100) NOT NULL ,
    mail VARCHAR(100) ,
    pass VARCHAR(50) NOT NULL ,
    course INTEGER REFERENCES courses(id)
);
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
