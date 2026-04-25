
from pydantic import BaseModel, EmailStr, AnyUrl, Field 
from typing import List , Dict, Optional, Annotated 
class Employee(BaseModel):
    name: str = Annotated[str, Field(max_length=50, title='Name of the employee', description='Give the name of the employee in less than 50 chars',examples=['Souvik','Shrimoyi'])]
    age: int = Annotated[int, Field(gt=18, lt=60, strict=True, description='Age must be between 18-60')]
    email: EmailStr 
    linkedin_url: AnyUrl
    weight: float = Annotated[float, Field(gt=0, strict=True)]
    married: bool = False   # by default false
    allergies: Optional[List[str]]  = None  # optional, if not given then None
    contact_details: Dict[str,str]

def add_employee_data(employee:Employee):
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.linkedin_url)
    print(employee.weight)
    print(employee.married)
    print(employee.allergies)
    print(employee.contact_details)

employee_info = {'name':'Souvik','age':22,'email':'souvikbag123@gmail.com','linkedin_url':'https://www.linkedin.com/in/souvik-b-8583982a5/','weight':60.0,'married':False,'contact_details':{'phone':'9876543210'}}

employee1 = Employee(**employee_info)

add_employee_data(employee1)





