from fastapi import FastAPI

app = FastAPI()

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