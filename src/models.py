from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped


Base = declarative_base()

class Teacher(Base):
    __tablename__="teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)

class Group(Base):
    __tablename__="groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group, backref="students")

class Subject(Base):
    __tablename__="subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship(Teacher, backref='subjects')

class Grade(Base):
    __tablename__="grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date = Column(DateTime, default=func.now)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship(Student, backref='grades')
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship(Subject, backref='grades')
