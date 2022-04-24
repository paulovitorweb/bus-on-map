from fastapi import FastAPI

from src.schemas import PositionSchema
from src.domain import Position
from src.adapters import stream, init_stream


app = FastAPI()


init_stream()


@app.post('/positions/')
def receive_position(position: PositionSchema):
    new_position = Position(**position.__dict__)
    stream(new_position)
