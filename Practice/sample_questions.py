print([(x, x+1) for x in range(1, 6)])


class Father():
    name = 'Robert'


class Person(Father):

    def __init__(self, name):
        self.fathername = super.name
        self.name = name

    def introduce(self):
        print("My name is", self.name, "son of", self.fathername)


king = Person("Joffrey")
king.introduce()
