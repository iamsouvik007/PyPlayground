

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator 
from typing import List , Dict, Optional, Annotated

class Employee(BaseModel):
    name: str 
    email: str 
    age: int 
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod 
    def email_validator(cls,value):
        valid_domains = ['icici.com','hdfc.com']
        domain_type = value.split('@')[-1]

        if domain_type not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value 
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 18 < value < 60:
            return value
        else:
            raise ValueError('Age should be in between 18 and 60')

def update_employee_data(employee: Employee):

    print(employee.name)
    print(employee.age)
    print(employee.allergies)
    print(employee.married)
    print('updated')

employee_info = {'name':'rohit', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'9876543210'}}

employee1 = Employee(**employee_info) # validation -> type coercion

update_employee_data(employee1)



