# Import FastAPI to create a simple web server
from fastapi import FastAPI, HTTPException 

# If you have additional routers, they can be included here as well
# from .routers import example_router

# Initialize the FastAPI application
app = FastAPI()

# Define a basic home route to check if the server is running
@app.get("/")
def read_root():
    """
    Root endpoint that confirms the API is working.
    This can be used to test if the FastAPI server is running properly.
    """
    return {"message": "Waving Pandas API is running!"}

# To run the server, use the following command in the terminal:
# uvicorn main:app --reload
