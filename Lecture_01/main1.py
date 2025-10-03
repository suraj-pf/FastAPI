from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , EmailStr ,AnyUrl, Field
from typing import List,Dict,Optional,Annotated

app = FastAPI()

class Patients(BaseModel):

    name : Annotated[str, Field(max_length=50,description="Enter the first name and last name of the patients",examples=["Suraj More","Sandeep More"])]
    age : int = Field(gt=0,lt=120)
    email : Optional[EmailStr]
    linkedIn : Optional[AnyUrl]
    weight : Annotated[float , Field(description="weight of the patient",strict=True)] #strict=True
    height : Annotated[float , Field(description="weight of the patient",gt=0)] #strict=True
    married : Annotated[bool , Field(default=False)]
    allergies : Annotated[List[str],Field(description="allegries the patient has or to be known",max_length=5,default=None)]
    contact_details: Optional[dict[str, str]] = None
    
patient_info = {
    "name": "suraj",
    "age": 21,
    "email" : "abk@gmail.com",
    "linkedIn" : "www.https:linkedIn/suraj-more",
    "weight": 70.5,
    "height": 175.0,
    "married": True ,
    "allergies": ["pollen", "dust","pollen", "dust","pollen"],
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
    print(patient.weight)
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
