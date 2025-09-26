from fastapi import FastAPI,Path,HTTPException
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
def sort_patient(sort_by: str,Path=(description=))