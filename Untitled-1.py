# базовый класс:
class Mentor:
    # конструктор:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return (self.firstName + ' ' + self.lastName)


# производный класс:
class Lecturer(Mentor):
    def __init__(self, firstName, lastName, Course):
        super().__init__(firstName, lastName)
        self.Course = []
        self.Course = Course

    def getCourse(self):
        return self.Course

# производный класс
class  Reviewer(Mentor):
    def __init__(self, firstName, lastName, Experts):
        super().__init__(firstName, lastName)
        self.Experts =  Experts

    def getExperts(self):
        return self.Experts


lecturer1 = Lecturer("Тимур", "Анвартдинов", "Python, знакомство с консолью")
print(lecturer1.firstName, lecturer1.lastName, lecturer1.Course)

lecturer2 = Lecturer("Олег", "Булыгин", "Основы языка программирования Python")
print(lecturer2.firstName, lecturer2.lastName, lecturer2.Course)

lecturer3 = Lecturer("Алёна", "Батицкая", "GIT - система контроля версий")
print(lecturer3.firstName, lecturer3.lastName, lecturer3.Course)



Reviewer1 = Reviewer("Ксения", "Дементьева", "Python, знакомство с консолью")
print(Reviewer1.firstName, Reviewer1.lastName, Reviewer1.Experts)

Reviewer2 = Reviewer("Олег", "Пустовалов", "Python, знакомство с консолью")
print(Reviewer2.firstName, Reviewer2.lastName, Reviewer2.Experts)

Reviewer3 = Reviewer("Сергей", "Быков", "Python, знакомство с консолью")
print(Reviewer3.firstName, Reviewer3.lastName, Reviewer3.Experts)

Reviewer4 = Reviewer("Денис", "Рудаков", "Python, знакомство с консолью")
print(Reviewer4.firstName, Reviewer4.lastName, Reviewer4.Experts)

Reviewer5 = Reviewer("Алёна", "Батицкая", "GIT - система контроля версий")
print(Reviewer5.firstName, Reviewer5.lastName, Reviewer5.Experts)