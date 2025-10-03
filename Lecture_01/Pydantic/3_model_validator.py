from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , EmailStr ,AnyUrl, Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

app = FastAPI()

class Patients(BaseModel):

    name : Annotated[str, Field(max_length=50,description="Enter the first name and last name of the patients",examples=["Suraj More","Sandeep More"])]
    age : int = Field(gt=0,lt=120)
    email : EmailStr
    linkedIn : Optional[AnyUrl]
    weight : Annotated[float , Field(description="weight of the patient",strict=True)] #strict=True
    height : Annotated[float , Field(description="weight of the patient",gt=0)] #strict=True
    married : Annotated[bool , Field(default=False)]
    allergies : Annotated[List[str],Field(description="allegries the patient has or to be known",max_length=5,default=None)]
    contact_details: Optional[dict[str, str]] = None

    @model_validator(mode="after")
    def check_emergency_contact(cls,model):
        if (model.age > 60) and ('emergency' not in model.contact_details):
            raise ValueError("Patient with age more than 60 should have emergency contact")
        else:
            return model

# field_validatior
patient_info = {
    "name": "suraj ",
    "age": '100',
    "email" : "suraj@hdfc.com",
    "linkedIn" : "www.https:linkedIn/suraj-more",
    "weight": 70.5,
    "height": 175.0,
    "married": True ,
    "allergies": ["pollen", "dust","pollen", "dust","pollen"],
    "contact_details": {
        "email": "suraj@example.com",
        "phone": "1234567890",
        "emergency":'7448096113'
    }
}

patient = Patients(**patient_info)

def update_patients_info(patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(f"Updated Info -")

update_patients_info(patient)
