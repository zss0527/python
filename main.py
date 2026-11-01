from fastapi import FastAPI

app = FastAPI(title="Demo", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}



@app.get("/hello/{name}")
def say_hello(name: str):
    print(f"Received request for name: {name}")
    return {"msg": f"Hello, {name}"}