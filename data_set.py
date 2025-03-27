from model.class_room import ClassRoom
from model.professor import Professor
from model.student import Student


class Dataset:

    def __init__(self):
        prof_math = Professor(id=1,firstname="Jean",lastname="MICHEL",age=44,subject="MATH")
        prof_fr = Professor(id=2,firstname="Elise",lastname="DUPONT",age=32,subject="FRENCH")
        prof_en = Professor(id=3,firstname="Léon",lastname="LAKE",age=52,subject="ENGLISH")
        prof_sport = Professor(id=4,firstname="Jane",lastname="DOE",age=27,subject="SPORTS")
        self._professors = [prof_math, prof_fr, prof_en, prof_sport]

        student_1 = Student(id=1, firstname="Kevin", lastname="JEAN", age=16,notes=[])
        student_2 = Student(id=2,firstname="Ludivine",lastname="Martinet",age=16,notes=[])
        student_3 = Student(id=3, firstname="Moussa", lastname="Konaté", age=15, notes=[])
        student_4 = Student(id=4, firstname="Laurant", lastname="Calonne", age=17, notes= [])
        student_5 = Student(id=5, firstname="Lise", lastname="JUIN", age=16, notes=[])
        student_6 = Student(id=6, firstname="Elise", lastname="SANDRE", age=16, notes=[])
        student_7 = Student(id=7, firstname="Louis", lastname="PARIS", age=16, notes=[])
        self._students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7]

        class_room_1_a = ClassRoom(id=1, name="1A", head_teacher=prof_math.id, students=[student_1, student_2])
        class_room_1_b = ClassRoom(id=2, name="1B", head_teacher=prof_en.id, students=[student_3, student_4])
        class_room_1_c = ClassRoom(id=3, name="1C", head_teacher=prof_sport.id, students=[student_4, student_5])
        self._classes = [class_room_1_a, class_room_1_b, class_room_1_c]

    @property
    def professors(self):
        return self._professors

    @property
    def students(self):
        return self._students

    @property
    def classes(self):
        return self._classes
