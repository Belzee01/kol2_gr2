#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from random import randint


class Classes(object):
    def __init__(self, students, absent):
        self.students = students
        self.absent = absent

    def add_grades(self):
        for student in self.students:
            student["grades"].append(randint(1, 6))


class Highschool(object):
    def __init__(self):
        self.classes = []

    def average(self):
        student_grades = []
        for clas in self.classes:
            for stud in clas.students:
                student_grades.extend(stud["grades"])

        return sum(student_grades) / len(student_grades)

    def class_average(self, c):
        class_grades = []
        for clas in self.classes:
            for stud in clas.students:
                if c == stud["clas"]:
                    class_grades.extend(stud["grades"])

        return sum(class_grades) / len(class_grades)

    def next_class(self, clas):
        self.classes.append(clas)
        for c in clas.students:
            c["attendance"] += 1


def main():
    students = [
        {"name": "Kajetan", "surname": "Lipensky", "clas": "1A", "grades": [], "attendance": 0},
        {"name": "Adam", "surname": "Nowak", "clas": "1B", "grades": [], "attendance": 0},
        {"name": "Tomasz", "surname": "Laz", "clas": "1A", "grades": [], "attendance": 0},
        {"name": "Szymon", "surname": "Kubasiak", "clas": "1B", "grades": [], "attendance": 0},
        {"name": "Krzysztof", "surname": "Jamrog", "clas": "1A", "grades": [], "attendance": 0}
    ]

    school = Highschool()

    present_list = list(students)
    present_list.remove(students[1])

    clas1 = Classes(present_list, [students[1]])
    clas1.add_grades()
    clas1.add_grades()

    school.next_class(clas1)

    present_list = list(students)
    present_list.remove(students[1])
    present_list.remove(students[3])
    clas2 = Classes(present_list, [students[1], students[3]])
    clas2.add_grades()
    school.next_class(clas2)

    print("Average grades for 1A: " + str(school.class_average("1A")))

    print("General students average: " + str(school.average()))

    print("Total attendance for first student: " + str(students[0]["attendance"]))

    print("Total attendance for second student: " + str(students[1]["attendance"]))


if __name__ == "__main__":
    main()
