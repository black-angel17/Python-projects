from abc import ABC,abstractmethod
# creating a template for the other uses
class User(ABC):
    class_varibale = 0  # this is for all the users

    def __init__(self,name,pawd):
        self.name  = name  #instance varibale
        self.pawd = pawd
        User.class_varibale = User.class_varibale + 1
        self.register()

    def register(self):
        print("New register found")

    def login(self):
        print("loggin in the user")
        return self




class Student(User):

    def welcome(self):
        print(self.name + " welmcome")


class Teacher(User):

    def welcome(self):
        print(self.name + " welmcome")


class Parents(User):

    def welcome(self):
        print(self.name + " welmcome")


def panni():
    print("apnad")



user1 = User("panni", "savvu")

#now user 1 is a real object now im passing this to an varible

dummy_obj = user1  # this like giving the address to a pointer variable

print(dummy_obj.name + "--------this is dummy")

# this is happening on there this like object is retuned


user2 = User("panni", "savvu")

print(user1.pawd)
user1.register()
print(User.class_varibale)

user2.class_varibale = 10 # even with the object we set value to class variable


#  user2.welcome() ---  will not work  cant call that child method


stu1 = Student("kunju", "small")
stu1.welcome()

stu1.register()

stu1.login().register()

print(__name__)
