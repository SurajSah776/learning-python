# Getter and Setter function illustration

class Person:
    def __init__(self, name):
        self._name = name

    # Getter
    @property
    def name(self):
        print('Getting name')
        return self._name

    # Setter
    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


# Creating Object
p = Person('Suraj')
print('The name is:', p.name)
p.name = 'Sunil'
del p.name
