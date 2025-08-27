from pydantic import BaseModel,EmailStr,Field, field_validator  
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title = 'Name of the patient',description = 'Give name of the patient under 50 chars')]
    age:int = Field(gt =18, le =25)
    email: EmailStr
    weight : Annotated[float, Field(gt =0, strict = True)]
    married : bool
    allergies : Annotated[Optional[List[str]],Field(default = None , max_length =5)]
    contact_info:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['cuilahore.edu.pk','code-graphers.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age', mode= 'before')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age must be in between 0 and 100")

patient_info = {'name':'zohaib','age': 22,'weight':90.5,'married':False, 'allergies':['pollen','dust'],'contact_info':{'email':'zohaibf595@gmail.com','number':'0302912094'}}
patient_info2 = {'name':'zohaib','email':'sp21-bcs-018@cuilahore.edu.pk','age': '22','weight':90.5,'married':False,'contact_info':{'number':'0302912094'}}
patient1= Patient(**patient_info2)

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)


insert_patient_data(patient1)