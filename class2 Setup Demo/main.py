from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello():
    return {"message":"Hello World"}

@app.get("/about")
def about():
    return {"message":"RP STUDY POINT is very useful channel for basic maths."}

