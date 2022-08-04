# Creating a simple OOP program

from datetime import date


class Employee():

    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod                                                # does not take any self/class parameters
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.06

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# printing values
# print(Employee.no_of_emps)
emp_1 = Developer('Corey', 'Schafer', 50000, 'Python')
emp_2 = Developer('Test', 'User', 60000, 'Java')

print(emp_1.fullname())  # need () if it is a method/function
print(emp_2.fullname())

print(emp_1.email)   # no need of () for variables
print(emp_2.email)

# print(Employee.no_of_emps)

emp_1.apply_raise()
print(emp_1.pay)

emp_2.raise_amount = 1.05
emp_2.apply_raise()

print(emp_2.pay)

Employee.set_raise_amount(1.05)
print(emp_1.raise_amount)

# If we have a sample string to parse all the data to create an instant we can use classmethod for this purpose

emp_new_str = 'John-Doe-55000'
emp_new = Employee.from_string(emp_new_str)

print(emp_new.email)


day = date.today()


print(emp_1.is_workday(day))


mgr_1 = Manager('sue', 'sam', 65000, [emp_1])

print(mgr_1.email)


mgr_1.add_emp(emp_2)
mgr_1.remove_emp(emp_1)

mgr_1.print_emps()

print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
