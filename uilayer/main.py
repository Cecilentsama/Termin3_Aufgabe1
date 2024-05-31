from datetime import date
import streamlit as st
from businesslayer.person import Person
from businesslayer.businesslayer import BusinessLayer
from common.common import person_list_as_dataframe
from common.functions import age_from_date
from uilayer.labels import LABEL_FIRSTNAME, LABEL_LASTNAME, LABEL_BIRTHDATE
from uilayer.format import DATE_FORMAT
from common.backends import DATA_ACCESS_TYPE_PANDAS


KEY_BUSINESS_LAYER = "BusinessLayer"
KEY_SELECTED_PERSON = "SelectedPerson"
KEY_SELECTED_BACKEND = "SelectedBackend"
TAG_COURSE_DAY = "Termin 3 - Refactoring/Persistenz/Test - Pandas"


def person_list_change():
    selected_item_idx = [pos[0] for pos in st.session_state["person_list_change"]["edited_rows"].items() if pos[1]["Manage"]]
    selected_person_list = list()
    for idx in selected_item_idx:
        selected_person_list.append(st.session_state[KEY_BUSINESS_LAYER].get_person_list()[idx])
    if len(selected_person_list) > 0:
        st.session_state[KEY_SELECTED_PERSON] = selected_person_list[0]
    else:
        st.session_state[KEY_SELECTED_PERSON] = None


st.title(TAG_COURSE_DAY)
if KEY_SELECTED_BACKEND not in st.session_state:
    st.session_state[KEY_SELECTED_BACKEND] = DATA_ACCESS_TYPE_PANDAS
if KEY_BUSINESS_LAYER not in st.session_state:
    st.session_state[KEY_BUSINESS_LAYER] = BusinessLayer(data_access_type=st.session_state[KEY_SELECTED_BACKEND])
if KEY_SELECTED_PERSON not in st.session_state:
    st.session_state[KEY_SELECTED_PERSON] = None

st.write(f'Using backend: {st.session_state[KEY_SELECTED_BACKEND]}')
input_area = st.container(border=True)
out_area = st.container(border=True)
if st.session_state[KEY_SELECTED_PERSON]:
    firstname = input_area.text_input(label=LABEL_FIRSTNAME, value=st.session_state[KEY_SELECTED_PERSON].firstname)
    lastname = input_area.text_input(label=LABEL_LASTNAME, value=st.session_state[KEY_SELECTED_PERSON].lastname)
    col1, col2 = input_area.columns(2)
    birthdate = col1.date_input(label=LABEL_BIRTHDATE, min_value=date(1900, 1 , 1), max_value=date.today(),
                                format=DATE_FORMAT , value= st.session_state[KEY_SELECTED_PERSON].birthdate)
    col2.text_input(label="Alter", value=age_from_date(st.session_state[KEY_SELECTED_PERSON].birthdate), disabled=True)
    btn_click = input_area.button(label="update_Person")
    btn_delete = input_area.button(label="delete person")

    if btn_click:
            selected_person = st.session_state[KEY_SELECTED_PERSON]
            selected_person.firstname = firstname
            selected_person.lastname = lastname
            selected_person.birthdate = birthdate
            st.session_state[KEY_BUSINESS_LAYER].update_person(selected_person)
    if btn_delete:
        st.session_state[KEY_BUSINESS_LAYER].delete_person(st.session_state[KEY_SELECTED_PERSON])
else:
    firstname = input_area.text_input(label=LABEL_FIRSTNAME, value="")
    lastname = input_area.text_input(label=LABEL_LASTNAME, value="")
    col1, col2 = input_area.columns(2)
    birthdate = col1.date_input(label=LABEL_BIRTHDATE, min_value=date(1900,1,1), max_value=date.today(), format=DATE_FORMAT)
    col2.text_input(label="Alter", value=age_from_date(birthdate), disabled=True)
    if firstname and lastname:
        btn_click = input_area.button(label="Create Person")
        if btn_click:
            st.session_state[KEY_BUSINESS_LAYER].create_person(firstname=firstname, lastname=lastname, birthdate=birthdate)

if len(st.session_state[KEY_BUSINESS_LAYER].get_person_list()) > 0:
    column_config = {
        Person.PERSON_ATTRIBUTE_NAME_ID: st.column_config.TextColumn(label="ID"),
        Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME: st.column_config.TextColumn(label=LABEL_FIRSTNAME),
        Person.PERSON_ATTRIBUTE_NAME_LASTNAME: st.column_config.TextColumn(label=LABEL_LASTNAME),
        Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE: st.column_config.DateColumn(label=LABEL_BIRTHDATE, format=DATE_FORMAT),
    }
    df = person_list_as_dataframe(st.session_state[KEY_BUSINESS_LAYER].get_person_list())
    df["Manage"] = False
    out_area.data_editor(data=df, key="person_list_change", on_change=person_list_change,
                         use_container_width=True, hide_index=True,
                         column_order=["Manage", Person.PERSON_ATTRIBUTE_NAME_LASTNAME, Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME,
                                       Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE, Person.PERSON_ATTRIBUTE_NAME_ID],
                         disabled=[Person.PERSON_ATTRIBUTE_NAME_LASTNAME, Person.PERSON_ATTRIBUTE_NAME_FIRSTNAME,
                                       Person.PERSON_ATTRIBUTE_NAME_BIRTHDATE, Person.PERSON_ATTRIBUTE_NAME_ID],
                         column_config=column_config)
