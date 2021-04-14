from datetime import date
import math

class Person:
	def __init__(self, name, year, month, day):
		self._name = name
		self._birthdate = date(year, month, day)

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, new_name):
		self._name = new_name

	@property
	def birthdate(self):
		return self._birthdate

	@birthdate.setter
	def birthdate(self, new_birthdate):
		self._birthdate = new_birthdate

	def get_age(self):
		return math.trunc((date.today() - self._birthdate).days / 365.25)


# Class Student inherits Class Person
class Student(Person):
	def __init__(self, *args, **kwargs):
		self._grades = []
		super().__init__(*args, **kwargs)

	def add_grade(self, new_grade):
		if not type(new_grade) is int or new_grade < 1 or new_grade > 10:
			raise Exception('The grade must be an integer within the range [1..10]')
		self._grades.append(new_grade)

	def mean_grade(self):
		if len(self._grades) == 0:
			return float('NaN')

		result = 0
		for grade in self._grades:
			result += grade

		return round(result / len(self._grades), 2)


# Class Teacher Inherits class Person
class Teacher(Person):
	def __init__(self, *args, **kwargs):
		self.subjects = []
		self._salary = 1000
		super().__init__(*args, **kwargs)

	@property
	def salary(self):
		return self._salary

	@salary.setter
	def salary(self, s):
		raise Exception('You cannot directly modify the salary')

	def increase_salary(self):
		self._salary = round(self._salary * 1.25)
