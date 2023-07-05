from fastapi import FastAPI
from enum import Enum


app = FastAPI()

"""
Path parameters
The value of the path parameter item_id will be passed to your function as the argument item_id.
You can declare the type of path parameter in the function where the data conversion and data valiation is done automatically.
All the data validation is performed under the hood by Pydantic. 
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

"""
Order matters
When creating path operations, you can find situations where you have a fixed path.
Like /users/me, let's say that it's to get data about the current user.
And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.
"""
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

"""
Predefined values
If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.
"""
class ModelName(str, Enum):
    """
    ModelName
    By inheriting from str the API docs will be able to know that the values must be of type string.
    """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):# Path parameter using the enum class
    # The value of the path parameter will be an enumeration member
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # To get actual value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # You can return enum members from your path operation. They will converted to their corresponding values.
    return {"model_name": model_name, "message": "Have some residuals"}

