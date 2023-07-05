**WSGI vs ASGI**

WSGI handles requests synchronously, processing them one after the other, which can lead to slower performance if there are many requests. It has been the Python standard for a long time and is used by frameworks like Flask. 

ASGI, on the other hand, processes requests asynchronously, allowing them to be handled independently without waiting for others to finish. This approach improves performance and is used by frameworks like FastAPI. 

# Resources 
1. https://developer.vonage.com/en/blog/how-wsgi-vs-asgi-is-like-baking-a-cake


