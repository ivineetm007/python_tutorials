from fastapi import FastAPI

# FastAPI is a Python class that provides all the functionality for your API.
app = FastAPI()

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:
#
# the path /
# using a get operation
@app.get("/")
def index():
    # dict, list, singular values as str, int or Pydantic models (will come later)
    return {"message": "Hello World!"}

