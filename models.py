# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    disciplines = relationship('Discipline', back_populates='teacher')


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='disciplines')
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='disciplines')
    grades = relationship('Grade', back_populates='discipline')




class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship('Student', back_populates='group')
    disciplines = relationship('Discipline', back_populates='group')  # Add this line


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')  # Add this line


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
    discipline = relationship('Discipline', back_populates='grades')
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='grades')
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
