from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    age:int
    weight : float
    married : bool
    allergies : Optional[List[str]] = None
    contact_info:Dict[str,str]


patient_info = {'name':'zohaib','age': 22,'weight':90.5,'married':False, 'allergies':['pollen','dust'],'contact_info':{'email':'zohaibf595@gmail.com','number':'0302912094'}}
patient_info2 = {'name':'zohaib','age': 22,'weight':90.5,'married':False,'contact_info':{'email':'zohaibf595@gmail.com','number':'0302912094'}}
patient1= Patient(**patient_info2)

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)


insert_patient_data(patient1)