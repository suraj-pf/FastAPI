from pydantic import BaseModel,EmailStr,Field,AnyUrl,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    height : float
    email : EmailStr
    linkedIn : AnyUrl
    allergies : List[str]
    contact_details : Dict[str , str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi

patient_info = {
    "name": "suraj",
    "age": 21,
    "email" : "abk@gmail.com",
    "linkedIn" : "www.https:linkedIn/suraj-more",
    "weight": 70.5,
    "height": 1.7,
    "allergies": ["pollen", "dust","pollen", "dust","pollen"],
    "contact_details": {
        "email": "suraj@example.com",
        "phone": "1234567890"
    }
}

patient = Patient(**patient_info)

def update_patients_info(patient1):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.linkedIn)
    print(patient.allergies)
    print("BMI is ",patient.bmi)
update_patients_info(patient)
