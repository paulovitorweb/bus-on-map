import faust
from typing import List
from src.config import Config
from src.domain import Position
from src.stream import schemas
from src.lambdas.check_off_route import check_off_route
from src.lambdas.check_bus_bunching import check_bus_bunching
from src.lambdas.check_bus_exceeded_capacity import check_bus_exceeded_capacity


app = faust.App(
    Config.APP_ID, 
    broker=Config.KAFKA_BROKER
)

alerts_topic = app.topic(
    Config.ALERTS_TOPIC, 
    value_type=schemas.AlertRecord
)


@app.agent(Config.POSITIONS_TOPIC, value_type=schemas.PositionRecord)
async def stream_positions(positions: List[schemas.PositionRecord]):
    async for pos in positions:
        position = Position(pos.lat, pos.lng, pos.vehicle_id, pos.route_id, pos.correlation_key)

        off_route = check_off_route(position)
        if off_route:
            await alerts_topic.send(value=schemas.AlertRecord(**off_route.__dict__))

        bus_bunching = check_bus_bunching(position)
        if bus_bunching:
            await alerts_topic.send(value=schemas.AlertRecord(**off_route.__dict__))

        bus_exceeded_capacity = check_bus_exceeded_capacity(position)
        if bus_exceeded_capacity:
            await alerts_topic.send(value=schemas.AlertRecord(**off_route.__dict__))


if __name__ == '__main__':
    app.main()