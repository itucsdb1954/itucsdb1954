import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """
    CREATE TABLE attendances(
    id INTEGER PRIMARY KEY ,
    upper_limit_percent INTEGER ,
    total_hour INTEGER ,
    attendance_hour INTEGER ,
    is_important BOOLEAN
);
""",
"""
CREATE TABLE homeworks(
    id INTEGER PRIMARY KEY ,
    number_of_homework INTEGER ,
    homework_weight INTEGER ,
    homework_score INTEGER ,
    is_important BOOLEAN
);
""",
"""
CREATE TABLE midterms(
    id INTEGER PRIMARY KEY ,
    number_of_midterm INTEGER ,
    midterm_weight INTEGER ,
    midterm_score INTEGER ,
    is_important BOOLEAN
);
""",
"""
CREATE TABLE projects(
    id INTEGER PRIMARY KEY ,
    number_of_project INTEGER ,
    project_weight INTEGER ,
    project_score INTEGER ,
    is_important BOOLEAN
);
""",
"""
CREATE TABLE vf_conditions(
    id INTEGER PRIMARY KEY ,
    attendance INTEGER REFERENCES attendances(id),
    midterm INTEGER REFERENCES midterms(id),
    homework INTEGER REFERENCES homeworks(id),
    project INTEGER REFERENCES projects(id)
);
""",
"""
CREATE TABLE courses(
    id INTEGER PRIMARY KEY ,
    department VARCHAR(50) NOT NULL ,
    course_name VARCHAR(100) NOT NULL ,
    course_description VARCHAR(100) ,
    lecturer_name VARCHAR(100) ,
    vf_condition INTEGER REFERENCES vf_conditions(id)
);
""",
"""
CREATE TABLE users(
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
