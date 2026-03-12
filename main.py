class Human:
    height = 180
    name1 = "KATE"
    name2 = "DRAKE"
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
jon = Worker()
print(nick.name1)
print(jon.name2)