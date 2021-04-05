class Employee:
    """A sample Employee class"""

def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.pay = pay

@property
def email(self):
    return '{}.{}@email.com'.format(self.first_name, self.last_name)

@property
def fullname(self):
    return '{}.{}'.format(self.first_name, self.last_name)


def __repr__(self):
    return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)