from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.schemas import PositionSchema
from src.domain import Position
from src.adapters import stream, init_stream


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


init_stream()


@app.post('/positions/')
def receive_position(position: PositionSchema):
    new_position = Position(**position.__dict__)
    stream(new_position)
