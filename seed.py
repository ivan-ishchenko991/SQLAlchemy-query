from faker import Faker

from src.models import Group, Student, Teacher, Subject, Grade
from src.db import session
from random import randint, choice

fake = Faker()

fake_groups = [fake.company() for _ in range(3)]
groups = []
for g in fake_groups:
    group = Group(name=g)
    groups.append(group)
    session.add(group)

fake_teachers = [fake.name() for _ in range(5)]
teachers = []
for t in fake_teachers:
    teacher = Teacher(fullname=t)
    teachers.append(teacher)
    session.add(teacher)

fake_subjects = ['English', 'physics', 'chemistry',
                 'math', 'Ukrainian language', 'geography', 'history']
subjects = []
for name in fake_subjects:
    subject = Subject(name=name, teacher=choice(teachers))
    subjects.append(subject)
    session.add(subject)

fake_students = [fake.name() for _ in range(30)]
students = []
for i in fake_students:
    student = Student(fullname=i, group=choice(groups))
    students.append(student)
    session.add(student)
    for subject in subjects:
        num_of_grades = randint(1, 20)
        for _ in range(num_of_grades):
            grade = Grade(grade=randint(1, 12), subject=subject,
                          student=student, date=fake.date_between(start_date="-1y"))
            session.add(grade)

session.commit()
