##OpenAPI

FastAPI uses the OpenAPI standard to generate a schema for your API. A schema is an abstract description of your API, including paths and parameters. OpenAPI defines the schema using JSON Schema, which specifies the structure and data types of JSON content. FastAPI automatically creates an openapi.json file that contains a detailed description of your API. You can access this file to examine the schema at http://127.0.0.1:8000/openapi.json. Understanding the schema helps you comprehend your API's structure and enables seamless integration with other tools or services.

**Path inside path parameters**

OpenAPI doesn't support a way to declare a path parameter to contain a path inside, as that could lead to scenarios that are difficult to test and define.  Nevertheless, you can still do it in FastAPI, using one of the internal tools from Starlette.
And the docs would still work, although not adding any documentation telling that the parameter should contain a path.

# Resources
1. https://fastapi.tiangolo.com/tutorial/first-steps/



