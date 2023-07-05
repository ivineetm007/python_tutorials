from fastapi import FastAPI
from typing import Union


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
Query parameters
The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
As they are part of the URL, they are "naturally" strings.
 As query parameters are not a fixed part of a path, they can be optional and can have default values.
"""
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""
Required and optional query parameters
You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
And you don't have to declare them in any specific order and will be detected by name.
"""
@app.get("/user_items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None# needy is required, skip has default value and limit is optional
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
