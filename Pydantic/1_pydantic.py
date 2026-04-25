
from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    blood_type: str

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.blood_type)

patient_info = {'name':'Rahul','age':30,'blood_type':'O negative'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)




















