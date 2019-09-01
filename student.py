# Practice: Solid Student
# Define a Python class named Student. This class will have 5 properties.

# First name(string)
# Last name(string)
# Age(integer)
# Cohort number(integer)
# Full name(read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.


class Student:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort = 0

    # first name getter and setter
    @property  # The getter
    def first_name(self):
        try:
            return self.__first_name  # Note there are 2 underscores here
        except AttributeError:
            return "no first name"

    @first_name.setter  # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for first name')

    # last name getter and setter
    @property  # The getter
    def last_name(self):
        try:
            return self.__last_name  # Note there are 2 underscores here
        except AttributeError:
            return "no last name"

    @last_name.setter  # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for last name')

    # age getter and setter
    @property  # The getter
    def age(self):
        try:
            return self.__age  # Note there are 2 underscores here
        except AttributeError:
            return "no age"

    @age.setter  # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for age')

    # cohort getter and setter
    @property  # The getter
    def cohort(self):
        try:
            return self.__cohort  # Note there are 2 underscores here
        except AttributeError:
            return "no cohort number assigned"

    @cohort.setter  # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide a integer value for cohort')

    # fullname getter
    @property  # The getter
    def fullname(self):
        try:
            # Note there are 2 underscores here
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return "enter a valid value for both first name and last name"
