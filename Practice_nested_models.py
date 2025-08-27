from pydantic import BaseModel

class Address(BaseModel):
    city :str
    state: str
    pin : str 

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address


address_dict = {'city':'lahore','state':'punjab','pin':'54000'}
address = Address(**address_dict)

patient_dict = {'name':'zohaib','gender':'male','age':22,'address':address}
patient = Patient(**patient_dict)

print(patient)
print(patient.name)
print(patient.address.city)