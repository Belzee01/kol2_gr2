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

class Classes(object):
	def __init__(self):
		self.attendace = 0
		self.score = 0
		
	def add_score(score):
		self.score = score
		
	def add_attendance(attendance):
		self.attendance = attendance
		
	def get_score():
		return self.score
		
	def get_attendance():
		return self.attendance

class Student(object):
	classes = []
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.ill = False
		
	def add_score_from_class(score, classes):
		cl = self.classes.index(classes)
		cl.add_score(score)
		
	def add_attendance_on_class(attendance, classes):
		cl = self.classes.index(classes)
		cl.add_attendance(attendance)
		
	def get_average_score():
		result = 0
		size = 0
		for i in classes:
			if i.get_score() != 0:
				result += i.get_score()
				size++
			
		return result/size
		
	def get_total_attendance():
		result = 0;
		for i in classes:
			if i.get_attendance() != 0:
				result += i.get_attendance()
			
		return result
		
	def check_if_student_ill():
		return self.ill
		

class Highschool(object):
	students = []
	def __init__(self):
		self.classes = 1;
		
	def add_student(student):
		self.students.append(student)
		
	def get_student(student):
		return self.students.index(student)
		
	def get_student_average_score(student):
		stud = self.students.index(student)
		return stud.get_average_score()
		
	def get_student_total_attendance(student):
		stud = self.students.index(student)
		return stud.get_total_attendance()
		
	def add_score_for_student(student, score):
		stud = self.students.index(student)
		stud.add_score_from_class(score, self.classes)
		
	def next_class():
		self.classes++
		for i in students:
			if i.check_if_student_ill() == True:
				i.add_attendance(self.classes)
			
	def check_if_student_passes(student):
		stud = self.students.index(student)
		if stud.get_average_score() > 2.0 and stud.get_total_attendance() > 0.9*classes:
			return True
		
		return False
		
def main():
	highschool = Highschool()
	
	stud1 = Student("Student1", "Nazwisko1")
	stud2 = Student("Student2", "Nazwisko2")
	stud3 = Student("Student3", "Nazwisko3")
	highschool.add_score_for_student(stud1, 3.0)
	

if __name__ == "__main__":
	main()

