from pydantic import BaseModel,EmailStr,Field,AnyUrl,computed_field,SerializeAsAny
from typing import List,Dict



class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str = "male"
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
    # 'gender' : 'male',
    "address" : address1
    
}

patient = Patient(**patient_info)

print(patient)

# temp = patient.model_dump(include=['name','gender'])

# temp = patient.model_dump(exclude={'address':['state']} )
temp = patient.model_dump(exclude_unset=True)





print(temp,type(temp))