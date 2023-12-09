# seed.py
from faker import Faker
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Teacher, Discipline, Group, Student, Grade
from datetime import datetime, timedelta
from random import randint

fake = Faker()

# Connect to the database
engine = create_engine('sqlite:///hw_module_7.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



def seed_data():
    # Drop existing tables
    Base.metadata.drop_all(engine)

    # Create tables
    Base.metadata.create_all(engine)

    # Seed Teachers
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    # Seed Disciplines
    disciplines = [
        Discipline(name="Mathematics", teacher_id=randint(1, 5)),
        Discipline(name="Programming", teacher_id=randint(1, 5)),
        Discipline(name="History", teacher_id=randint(1, 5)),
        Discipline(name="Geometry", teacher_id=randint(1, 5)),
        Discipline(name="English", teacher_id=randint(1, 5)),
        # Add more disciplines as needed
    ]
    session.add_all(disciplines)
    session.commit()

    # Seed Groups
    groups = [Group(name=fake.random_element(['Group A', 'Group B', 'Group C', 'Group D'])) for _ in range(4)]
    session.add_all(groups)
    session.commit()

    # Seed Students
    students = [Student(fullname=fake.name(), group_id=randint(1, 4)) for _ in range(50)]
    session.add_all(students)
    session.commit()

    # Seed Grades
    start_date = datetime.strptime('2022-09-01', "%Y-%m-%d")
    end_date = datetime.strptime('2024-06-20', "%Y-%m-%d")

    for _ in range(20):
        discipline_id = randint(1, 5)
        student_id = randint(1, 50)
        grade_value = randint(1, 12)
        date_of = fake.date_between(start_date=start_date, end_date=end_date)

        grade = Grade(discipline_id=discipline_id, student_id=student_id, grade=grade_value, date_of=date_of)
        session.add(grade)

    session.commit()


if __name__ == '__main__':
    seed_data()




