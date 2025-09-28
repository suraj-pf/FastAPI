from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , EmailStr ,AnyUrl, Field
from typing import List,Dict,Optional

app = FastAPI()

class Patients(BaseModel):

    name : str
    age : int
    email : Optional[EmailStr]
    linkedIn : Optional[AnyUrl]
    weight : float = Field(gt=0)
    height : float
    married : bool = True
    allergies : Optional[List[str]] = None
    contact_details: Optional[dict[str, str]] = None
    
patient_info = {
    "name": "suraj",
    "age": 21,
    "email" : "abk@gmail.com",
    "linkedIn" : "www.https:linkedIn/suraj-more",
    "weight": -70.5,
    "height": 175.0,
    # "married": False,
    # "allergies": ["pollen", "dust"],
    "contact_details": {
        "email": "suraj@example.com",
        "phone": "1234567890"
    }
}

patient = Patients(**patient_info)

@app.get("/")
def hello():
    return {'message':"Hello world!"}

@app.get("/about")
def about():
    return {
        "name":"suraj more",
        "age":23,
        "Occupation":"Business"
    }



def update_patients_info(patient1):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedIn)
    print(patient.allergies)
    print(patient.married)
    print(f"Updated Info -")

def insert_patients_info(patient : Patients):
    print(patient.name)
    print(patient.age)
    print("Updated patient info")

update_patients_info(patient)