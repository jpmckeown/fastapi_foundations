import json
from pydantic import BaseModel

class Car(BaseModel):
    size: str
    fuel: str | None = "electric"
    doors: int = 4
    transmission: str | None = "auto"

class CarOutput(Car):
        id: int


def load_db() -> list[CarOutput]:
    """Load a list of Car objects froma JSON file."""
    with open("cars.json") as f:
        return [CarOutput.model_validate(obj) for obj in json.load(f)]


def save_db(cars: list[CarOutput]):
    with open("cars.json", 'w') as f:
        json.dump([car.model_dump() for car in cars], f, indent=4)