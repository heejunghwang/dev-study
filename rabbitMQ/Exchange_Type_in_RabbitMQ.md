# Exchange Type in RabbitMQ

## Exchange 개념

* AMQP의 일부분
* 메시지를 Que에 라우팅(전달)하는 역할
* 라우팅 알고리즘은 exchange type과 bind 규칙에 따라 결정됨
* bind는 메시지 전달을 위한 큐로 exchange하는 역할을 함.

![exchange](https://www.rabbitmq.com/img/tutorials/intro/hello-world-example-routing.png)

## Exchange type in Rabbit MQ

| Name             | Default pre-declared names              |
| ---------------- | --------------------------------------- |
| Direct exchange  | (Empty string) and amq.direct           |
| Fanout exchange  | amq.fanout                              |
| Topic exchange   | amq.topic                               |
| Headers exchange | amq.match (and amq.headers in RabbitMQ) |

* Direct exchange
  * 메시지 라우팅 키를 기반으로 메시지를 큐에 전달

![directexchange](https://www.rabbitmq.com/img/tutorials/intro/exchange-direct.png)

* Fanout exchange
  * 메시지 브로드 캐스트 라우팅에 이상적
  * 예) 그룹 채팅은 팬 아웃 교환을 사용하여 참가자들간에 메시지를 배포

![fanout](https://www.rabbitmq.com/img/tutorials/intro/exchange-fanout.png)



