from fastapi import FastAPI
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

