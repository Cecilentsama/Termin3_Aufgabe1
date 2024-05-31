import pandas as pd
from businesslayer.person import Person
from datetime import date


def person_list_as_dataframe(person_list):
    return pd.DataFrame([person.as_dict() for person in person_list])


def dataframe_as_person_list(df):
    ret = list()
    for i in range(len(df)):
        ret.append(Person(firstname=df.loc[i, Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME], lastname=df.loc[i, Person.PERSON_ATTRIBUTE_NAME_LASTNAME],
                          birthdate=date.fromisoformat(df.loc[i, Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE]), id=df.loc[i, Person.PERSON_ATTRIBUTE_NAME_ID]))
    return ret
