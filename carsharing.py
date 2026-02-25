from fastapi import FastAPI

app = FastAPI()
db = [
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "diesel", "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"}
]

@app.get("/cars/")
async def get_cars(doors: int|None = None, size: str|None = None):
    """Retrieve all cars."""
    print("doors raw:", repr(doors), "type:", type(doors))
    print("size raw:", repr(size), "type:", type(size))
    result = db
    if size:
        result = [x for x in result if x['size'] == size]
    if doors:
        result = [x for x in result if x['doors'] == doors]
    return result

@app.get("/cars/{id}")
async def car_by_id(id):
    """Return one car selected by id."""
    print(type(id))
    result = [x for x in db if x['id'] == id]
    return result[0]


@app.get("/")
async def welcome(name):
    """Return a welcome message."""
    return {'message': f"Welcome, {name.upper()} to the Car Sharing service!"}

