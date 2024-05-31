from unittest import TestCase

from datalayer.dataaccess_pandas import DataAccessPandas
from businesslayer.person import Person
from datetime import date


def test_save():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person = Person(firstname="Max", lastname="Test", birthdate=date(2000, 1, 31))

    size_person_list_before = len(da_pandas.load_person_list())
    da_pandas.save_person(person)
    person_list_after = da_pandas.load_person_list()

    assert size_person_list_before < len(person_list_after)


def test_load_person_list():
    da_pandas = DataAccessPandas("test_pandas.csv")
    person_list = da_pandas.load_person_list()
    assert person_list is not None

    size_person_list_before = len(person_list)
    person = Person(firstname="Max", lastname="Test", birthdate=date(2000, 1, 31))
    da_pandas.save_person(person)
    person_list_after = da_pandas.load_person_list()
    assert size_person_list_before + 1 == len(person_list_after)


class testclass(TestCase):
    def test_update_person(self):
        self.assertEquals()
