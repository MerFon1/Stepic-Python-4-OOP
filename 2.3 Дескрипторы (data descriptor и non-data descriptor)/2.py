"""

"""


# DESCRIPTOR
class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_lenght = min_length
        self.max_length = max_length

    def validate(self, string):
        return self.min_lenght <= string <= self.max_length


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


validate = ValidateString(min_length=3, max_length=100)
st = StringValue(validator=ValidateString(3, 40))
