# the is the code to show how explicitly we create constructor.

class Student :
    def __init__(self, name, marks):  # this is the default constructor 
        self.name = name
        self.marks = marks  
        print("adding new student to the school's database")

s1 = Student("karan aujla", 58)
print (s1.name, s1.marks)

s2 = Student("arjun kapoor",60)
print(s2.name, s2.marks)

s3 = Student("salman khan", 98)
print(s3.name, s3.marks)


# Attribute = "variables and data
