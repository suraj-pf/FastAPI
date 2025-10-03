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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icic.com']
        #abc@gmail.com
        doman_name = value.split('@')[-1]

        if doman_name not in valid_domains:
            raise ValueError('Not a valid email')
        return value
    
    @field_validator('name',mode='after')
    @classmethod
    def name_capitalizer(cls, value):
        # Split the string by spaces and strip any leading/trailing spaces
        value = value.strip().split()
    
        if len(value) >= 1:
            # Capitalize the first and last words, and join them back
            value[0] = value[0].capitalize()
            value[-1] = value[-1].capitalize()
    
        # Join the string back into a single string with spaces
        return " ".join(value)

    @field_validator('age',mode='after')
    @classmethod
    def agec_checker(cls,value):
        if 0 < value < 120 :
            return value
        else:
            raise ValueError('Age should be between 0 and 120')

# field_validatior
patient_info = {
    "name": "suraj ",
    "age": '21',
    "email" : "suraj@hdfc.com",
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

def update_patients_info(patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(f"Updated Info -")

update_patients_info(patient)
