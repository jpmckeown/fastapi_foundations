from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome(name):
    """Return a welcome message."""
    return {'message': f"Welcome, {name.upper()} to the Car Sharing service!"}
