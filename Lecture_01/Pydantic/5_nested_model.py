from pydantic import BaseModel,EmailStr,Field,AnyUrl,computed_field
from typing import List,Dict



class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address

    
address_dict = {
    'city' : 'pune',
    'state' : 'Maharashtra',
    'pincode' : '410058'
}
address1 = Address(**address_dict)

patient_info = {
    "name": "suraj",
    "age": 21,
    'gender' : 'male',
    "address" : address1
    
}

patient = Patient(**patient_info)

print(patient)