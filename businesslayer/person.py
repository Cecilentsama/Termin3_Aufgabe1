from common.functions import age_from_date


class Person:
    PERSON_ATTRIBUTE_NAME_FIRSTNAME = "firstname"
    PERSON_ATTRIBUTE_NAME_LASTNAME = "lastname"
    PERSON_ATTRIBUTE_NAME_BIRTHDATE = "birthdate"
    PERSON_ATTRIBUTE_NAME_ID = "id"

    def __init__(self, firstname, lastname, birthdate, id=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    def age(self):
        return age_from_date(self.birthdate)

    def __str__(self):
        return f'Person: {self.firstname} {self.lastname} {self.birthdate}'

    def as_dict(self):
        return {
            Person.PERSON_ATTRIBUTE_NAME_ID: self.id,
            Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME: self.firstname,
            Person.PERSON_ATTRIBUTE_NAME_LASTNAME: self.lastname,
            Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE: self.birthdate
        }
