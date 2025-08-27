from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

patient_info = {'name':'zohaib','age': 22}
patient1= Patient(**patient_info)

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)

insert_patient_data(patient1)