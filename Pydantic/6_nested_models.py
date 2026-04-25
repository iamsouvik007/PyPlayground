
from pydantic import BaseModel 

class Address(BaseModel):
    city: str 
    state: str 
    zip: str 

class Employee(BaseModel):
    name: str 
    age: str 
    gender: str 
    address: Address 

address_info = {'city':'Kolkata', 'state':'West Bengal', 'zip':'700001'}
address1 = Address(**address_info)

employee_info = {'name':'Rohit', 'age':25,'gender':'Male','address':address1}

employee1 = Employee(**employee_info)

temp = employee1.model_dump(include={'address'})
print(type(temp))







