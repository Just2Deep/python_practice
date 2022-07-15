# using getter and setter property

class Employee():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return self.first.lower() + '.' + self.last.lower() + '@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting Employee Data')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.first = 'Jim'
emp_1.last = 'Halpert'

emp_1.fullname = 'Dwight Schrute'

print(emp_1.fullname)
print(emp_1.email)

# del emp_1.fullname  ## to use the deleter method
