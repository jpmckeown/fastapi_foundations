import json
from pydantic import BaseModel

class Car(BaseModel):
    id: int
    size: str
    fuel: str | None = "electric"
    doors: int = 4
    transmission: str | None = "auto"


def load_db() -> list[Car]:
    """Load a list of Car objects froma JSON file."""
    with open("cars.json") as f:
        return [Car.model_validate(obj) for obj in json.load(f)]


def save_db(cars: list[Car]):
    with open("cars.json", 'w') as f:
        json.dump([car.model_dump() for car in cars], f, indent=4)