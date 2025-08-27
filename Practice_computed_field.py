
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height:float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi 



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.calculate_bmi)
    print('updated')

patient_info2 = {'name':'zohaib','email':'sp21-bcs-018@cuilahore.edu.pk','age': 65,'weight':90.5,'height':1.72,'married':False,'allergies':['pollen','dust'],'contact_info':{'number':'0302912094'}}

patient1 = Patient(**patient_info2) 

update_patient_data(patient1)
