# my_select.py
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from models import Student, Grade, Base, Group, Discipline, Teacher
from sqlalchemy import func, and_

# Create the engine
engine = create_engine('sqlite:///hw_module_7.db')

# Bind the engine to the Base
Base.metadata.bind = engine

# Create a new session
session = Session(engine)


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def find_top_students():
    top_students = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )

    for student, average_grade in top_students:
        # print(f"1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
        print(f"Student: {student.fullname}, Average Grade: {average_grade}")


# 2.  Знайти студента із найвищим середнім балом з певного предмета.
def find_top_student_in_subject(subject_name):
    top_student = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade, and_(Student.id == Grade.student_id, Grade.discipline.has(name=subject_name)))
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )

    print(f"2. Top student in {subject_name}: {top_student[0].fullname}, Average Grade: {top_student[1]}")


# 3. Знайти середній бал у групах з певного предмета.

def find_average_grade_in_groups(subject_name):
    average_grades = (
        session.query(Group.name, func.avg(Grade.grade).label('average_grade'))
        .filter(Grade.discipline.has(name=subject_name))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .group_by(Group.name)  # Use Group class for grouping
        .all()
    )

    for group, average_grade in average_grades:
        print(f"{subject_name}")
        print(f"Group: {group}, Average Grade: {average_grade}")


# 4. Знайти середній бал на потоці (по всій таблиці оцінок).
def find_average_grade_overall():
    average_grade = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .scalar()
    )

    print(f"4. Overall Average Grade: {average_grade}")


# 5. Знайти які курси читає певний викладач:
def find_courses_by_teacher(teacher_name):
    courses = (
        session.query(Discipline.name)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name)
        .distinct()
        .all()
    )

    print(f"5. Courses taught by {teacher_name}: {', '.join(course[0] for course in courses)}")


# 6.  Знайти список студентів у певній групі:

def find_students_in_group(group_name):
    students = (
        session.query(Student.fullname)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )

    print(f"6. Students in group {group_name}: {', '.join(student[0] for student in students)}")

# 7. Знайти оцінки студентів у окремій групі з певного предмета:


def find_grades_in_group_for_subject(group_name, subject_name):
    grades = (
        session.query(Student.fullname, Grade.grade)
        .join(Group)
        .outerjoin(Grade, (Student.id == Grade.student_id) & Grade.discipline.has(name=subject_name))
        .filter(Group.name == group_name)
        .all()
    )

    print(f"7. Grades in {subject_name} for students in {group_name}:")
    for student, grade in grades:
        print(f"{student}: {grade}")

# 8.  Знайти середній бал, який ставить певний викладач зі своїх предметів:

def find_average_grade_by_teacher(teacher_name):
    average_grade = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name)
        .scalar()
    )

    print(f"8. Average Grade given by {teacher_name}: {average_grade}")


# 9.  Знайти список курсів, які відвідує певний студент:
def find_courses_by_student(student_name):
    courses = (
        session.query(Discipline.name)
        .join(Grade, Discipline.id == Grade.discipline_id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Student.fullname == student_name)
        .distinct()
        .all()
    )

    print(f"9. Courses attended by {student_name}: {', '.join(course[0] for course in courses)}")


# 10.  Список курсів, які певному студенту читає певний викладач:
def find_courses_taught_to_student(teacher_name, student_name):
    courses = (
        session.query(Discipline.name)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .join(Group, Discipline.group_id == Group.id)
        .join(Student, Group.id == Student.group_id)
        .join(Grade, and_(Grade.discipline_id == Discipline.id, Grade.student_id == Student.id))
        .filter(Teacher.fullname == teacher_name, Student.fullname == student_name)
        .distinct()
        .all()
    )

    print(f"List of courses taught by {teacher_name} to {student_name}:")
    for course in courses:
        print(course)

# 1. Додаткове Середній бал, який певний викладач ставить певному студентові.
def find_average_grade_by_teacher_and_student(teacher_name, student_name):
    average_grade = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Teacher.fullname == teacher_name, Student.fullname == student_name)
        .group_by(Student.id)
        .scalar()
    )

    print(f"Average grade given by {teacher_name} to {student_name}: {average_grade}")


if __name__ == '__main__':
    find_top_students()
    print(f"____________")
    find_top_student_in_subject("Programming")
    print(f"3. Знайти середній бал у групах з певного предмета.")
    find_average_grade_in_groups("Mathematics")
    print(f"____________")
    find_average_grade_overall()
    print(f"____________")
    find_courses_by_teacher("John Ibarra")
    print(f"____________")
    find_students_in_group("Group A")
    print(f"____________")
    find_grades_in_group_for_subject("Group A", "Mathematics")
    print(f"____________")
    find_average_grade_by_teacher("John Ibarra")
    print(f"____________")
    find_courses_by_student("David Calderon")
    print(f"____________")
    find_courses_taught_to_student("Amber Gay", "David Calderon")
    print(f"____________")
    find_average_grade_by_teacher_and_student('Amber Gay', 'David Calderon')

