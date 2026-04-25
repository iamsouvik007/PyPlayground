from pydantic import BaseModel, Field, computed_field
from typing import List, Dict

class Employee(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height **2), 2)
        return bmi 

def update_employee_data(employee: Employee):
    print(employee.name)
    print(employee.age)
    print(employee.allergies)
    print(employee.married)
    print(employee.bmi)
    print('updated')

employee_info = {'name':'mohit', 'age': '30', 'weight': 75.2, 'height': 1.75, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'9876543210'}}
employee1 = Employee(**employee_info)
update_employee_data(employee1)

