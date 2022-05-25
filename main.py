class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        summ, count = 0, 0
        for theme in self.grades.values():
            for i in theme:
                summ += i
                count += 1
        return round(summ / count, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.avg_grade()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def avg_grade(self):
        summ, count = 0, 0
        for theme in self.grades.values():
            for i in theme:
                summ += i
                count += 1
        return round(summ / count, 1)
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avg_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
best_student.finished_courses += ['Английский для программирования']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

nice_lector = Lecturer('Bob', 'Hunter')
nice_lector.courses_attached += ['Python']

best_student.rate_lec(nice_lector, 'Python', 10)
best_student.rate_lec(nice_lector, 'Python', 10)
best_student.rate_lec(nice_lector, 'Python', 9)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)
# print(nice_lector.grades)
# print(cool_reviewer)
# print(nice_lector)
print(best_student)