from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('Patients.json','r') as file:
        data = json.load(file)

    return data

@app.get("/")
def hello():
    return {'message':"A patient management API"}

@app.get("/about")
def about():
    return {
        "message":"An API to management Patient records "
    }

@app.get("/view")
def get_view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def get_record(patient_id: str = Path(...,description="ID of the patient is required as a path params",example="P001")):
    data = load_data()


    if patient_id in data :
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')

@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description="Field to sort patients by height,weight,bmi"),
                 order_by: str = Query("asc", description="Sort in ascending or descending order")):
    

    valid_field = ['height','weight','bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail="Invalid field select from {valid_field}") 
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Order not in ascding or descending")
    
    data = load_data()

    # in order to get the reverse in the sorted_patients line that means order by asc or desc 
    # False means ascending, True means descending
    sort_order = False if order_by == 'desc' else True

    # in order to get the sorted patients list
    sorted_patients = sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_patients