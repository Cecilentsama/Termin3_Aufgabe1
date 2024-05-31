from .person import Person
from datetime import date
from datalayer.dataaccess_pandas import DataAccessPandas
import common.backends


class BusinessLayer:
    STORAGE_FILE_NAME_PANDAS = "data.csv"
    STORAGE_FILE_NAME_SQLITE = "data.db"

    def __init__(self, data_access_type):
        match data_access_type:
            case common.backends.DATA_ACCESS_TYPE_PANDAS:
                self.data_access = DataAccessPandas(BusinessLayer.STORAGE_FILE_NAME_PANDAS)

    def create_person(self, firstname:str, lastname:str, birthdate:date):
        return self.data_access.save_person(Person(firstname=firstname, lastname=lastname, birthdate=birthdate))

    def update_person(self, person:Person):
        self.data_access.update_person(person)

    def delete_person(self, person:Person):
        self.data_access.delete_person(person)

    def get_person_list(self):
        return self.data_access.load_person_list()
