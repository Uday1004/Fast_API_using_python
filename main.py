from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Route 1: Hello World
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Route 2: Greeting with a name
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
