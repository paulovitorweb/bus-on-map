# Worker

Tem como objetivo executar funções que fazem verificações sobre as posições transmitidas pelo GPS dos veículos e gerar alertas no tópico 'alerts' do Kafka.

Por exemplo:

- check_out_of_route: verifica se o ônibus está fora de rota;
- check_bus_bunching: verifica se ônibus da mesma linha estão em comboio;
- check_bus_exceeded_capacity: verifica se o veículo excedeu a capacidade de transporte de passageiros.

Para diminuir o uso de recursos computacionais, pode-se definir um intervalo de tempo em que cada veículo será monitorado por cada função.
Por exemplo, a função que verifica se está fora de rota pode ser executada somente após 30 segundos da última verificação do mesmo veículo,
a função que verifica possíveis comboios, após 2 minutos, e a função que verifica se excedeu capacidade, após 1 minuto.

## Desenvolvimento

Crie um arquivo `.env` na pasta raiz do projeto.

```
REDIS_HOST=localhost
REDIS_PORT=6379
```

## Testes

Execute os testes.

```
make test
```