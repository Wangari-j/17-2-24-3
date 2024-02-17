class Employee:
    fullname = ""
    email = ""

    def __init__(self,firstname,lastname):
        self.fullname = firstname + lastname
        self.email = firstname + "." + lastname + "@company.com"

emp1 = Employee("Ann", "John")
emp2 = Employee("Mia", "Yan")

print(emp1.fullname)
print(emp2.email)