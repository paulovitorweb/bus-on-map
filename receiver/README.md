# Bus-on-map receiver

API responsible for receiving vehicle positions given by the onboard GPS.

This is an API written in Python with FastAPI.

## Development

With kafka broker running, run the server:

```
make run
```

## Test

This program uses the unittest package for unit tests. Run:

```
make test
```

## Docs

- With Swagger: http://127.0.0.1:8000/docs
- With ReDoc: http://127.0.0.1:8000/redoc