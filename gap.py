from abc import ABC, abstractmethod

# Класс Student остается неизменным
class Student:
    def init(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Класс для управления списком студентов
class StudentList:
    def init(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

# Принцип SRP: разделение ответственности
# Класс для расчета средней оценки студентов
class GradeCalculator:
    @staticmethod
    def get_average_grade(students):
        total = 0
        for student in students:
            total += student.grade
        return total / len(students) if students else 0

# Принцип SRP: разделение ответственности
# Класс для фильтрации студентов
class StudentFilter:
    @staticmethod
    def filter_students(students, strategy):
        return strategy.filter(students)

# Принцип OCP и DIP: использование интерфейсов и стратегий для фильтрации
class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, students):
        pass

class GradeAboveFilter(FilterStrategy):
    def init(self, grade):
        self.grade = grade

    def filter(self, students):
        return [student for student in students if student.grade > self.grade]

# Принцип LSP: новый фильтр для студентов с оценками ниже заданного
class GradeBelowFilter(FilterStrategy):
    def init(self, grade):
        self.grade = grade

    def filter(self, students):
        return [student for student in students if student.grade < self.grade]

# Пример использования
if name == "main":
    # Создаем список студентов
    student_list = StudentList()
    student_list.add_student(Student("John", 20, 90))
    student_list.add_student(Student("Jane", 21, 85))
    student_list.add_student(Student("Doe", 22, 70))

    # Расчет средней оценки
    average_grade = GradeCalculator.get_average_grade(student_list.students)
    print(f"Average grade: {average_grade}")

    # Фильтрация студентов с оценками выше 80
    filter_strategy = GradeAboveFilter(80)
    filtered_students = StudentFilter.filter_students(student_list.students, filter_strategy)
    print("Students with grades above 80:")
    for student in filtered_students:
        print(f"{student.name}: {student.grade}")

    # Фильтрация студентов с оценками ниже 90
    filter_strategy = GradeBelowFilter(90)
    filtered_students = StudentFilter.filter_students(student_list.students, filter_strategy)
    print("Students with grades below 90:")
    for student in filtered_students:
        print(f"{student.name}: {student.grade}")