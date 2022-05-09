# Worker

Tem como objetivo executar funções que fazem verificações sobre as posições transmitidas pelo GPS dos veículos e gerar alertas em tópico apropriado no Kafka.

Por exemplo:

- check_out_of_route: verifica se o ônibus está fora de rota;
- check_bus_bunching: verifica se ônibus da mesma linha estão em comboio;
- check_bus_exceeded_capacity: verifica se o veículo excedeu a capacidade de transporte de passageiros.

Para diminuir o uso de recursos computacionais, pode-se definir um intervalo de tempo em que cada veículo será monitorado por cada função.
Por exemplo, a função que verifica se está fora de rota pode ser executada somente após 30 segundos da última verificação do mesmo veículo,
a função que verifica possíveis comboios, após 2 minutos, e a função que verifica se excedeu capacidade, após 1 minuto.

## Configuração

Algumas variáveis de ambiente:

- LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE: distância máxima tolerada de onde o ônibus está para o ponto mais próximo da rota;
- CACHE_ROUTE_EXPIRATION_IN_SECONDS: tempo de expiração do cache da rota, em segundos.

## Desenvolvimento

Crie um arquivo `.env` na pasta raiz do projeto.

```
APP_ID=worker_app
POSITIONS_TOPIC=positions3
ALERTS_TOPIC=alerts
REDIS_HOST=localhost
REDIS_PORT=6379
KAFKA_BROKER=localhost:29092
POSTGRES_DB_HOST=localhost
POSTGRES_DB_PORT=5432
POSTGRES_DB_NAME=postgres
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASS=postgres
LAMBDA_MAX_DISTANCE_TOLERATED_OFF_ROUTE=50
LAMBDA_OFF_ROUTE_INTERVAL_IN_SECONDS=60
CACHE_ROUTE_EXPIRATION_IN_SECONDS=60
```

## Testes

Para executar os testes:

```
make test
```

## Stream de dados

Para iniciar o stream de dados, certifique-se de que está com o ambiente virtual ativado e execute:

```
faust -A src.main worker -l info
```
