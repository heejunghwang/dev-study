# Docker 기본

* Docker exec

  * 실행 중이 컨테이너를 들어가기 위한 방법

    ~~~
    docker exec -t -i 43k5ofdk3jf<컨테이너 ID> /bin/bash
    ~~~

* 도커 로그

  * 컨테이너 내부에서 stdout이나 stderr로 보내는 것들은 도커 데몬이 모두 캡쳐하여 각 컨테이너의 JSON 파일에 설정된 백엔드로 흘러가도록 하는 것
  * 필요할때마다 명령행 프롬프트에서 곧바로 로그를 원격에서 가져오므로 편리하며, 적은 분량의 로그만이 필요할 때 유용한 방식
  * 로그가 백업되고 있는 실제 파일은 도커 서버에 있음
    * 기본적으로 /var/lib/docker/containers/<container_id>에 저장됨
    * <container_id>부분은 실제 컨테이너 ID가 디렉터리명임.
  * 보통의 로그 파일처럼 docker logs -f를 사용하면 도커 로그의 최신 부분을 실시간으로 볼 수 있음.

  ~~~
  docker logs
  ~~~

  * 위의 방식은 단일 호스트의 로깅에는 괜찮음. 로그에 대한 원격 접근이 어렵고 대용량 로그에 대한 공간 사용 등의 결점이 존재
  * 도커는 이를 설정이 가능한 로깅 백엔드를 지원 : syslog, fluentd, journal, gelf, awslogs, splunk등임.
  * syslog를 많이 사용하는데, 도커 명령행 옵션에서 --log-driver=syslog 옵션을 주어서 쓸 수 있다.
  * 그외 방법
    * 사용자 애플리케이션에 직접 로깅
    * 컨테이너 안에 로그를 릴레이해주는 프로세스 매니저를 둔다.(systemd, upstart, supervisor, runit 등)
    * 컨테이너에서 stdout/stderr을 감싸도록 로깅 릴레이를 실행
    * 도커 JSON 로그 자체를 서버나 다른 컨테이너에서 원격 로깅 프레임워크로 보낸다.



# Docker Compose

* Docker 컴포즈 인프라 구성 파일 : docker-compose.yml

* Docker Compose 커맨드

  | 커맨드  | 설명                        |
  | ------- | --------------------------- |
  | up      | 컨테이너 생성 및 구동       |
  | scale   | 생성할 컨테이너 개수 지정   |
  | ps      | 컨테이너 목록 확인          |
  | logs    | 컨테이너 로그 출력          |
  | run     | 컨테이너 실행               |
  | start   | 컨테이너 구동               |
  | stop    | 컨테이너 중지               |
  | restart | 컨테이너 재가동             |
  | Kill    | 실행중이 컨테이너 강제 종료 |

  

* Docker 커멘드는 docker-compse.yml을 지정한 디렉터리에에서 실행함. 현재 디렉터리가 아닌 다른 디렉터리에서 docker-compse.yml을 실행해야하는 경우에는 f옵션으로 파일 경로를 지정

  ~~~
  docker-compose -f ./sample/docker-compose.yml up
  ~~~

* 특정 컨테이너 중지

  ~~~~
  docker-compose stop <컨테이너명>
  ~~~~

  

* 여러 커멘드를 한번에 생성(up)

  * 여러 컨테이너를 생성하고 구동할 때는 docker-compose up 커멘드 사용
  * 옵션
    * -d : 백그라운드에서 실행
    * —no-deps : 링크된 서비스를 구동하지 않음
    * —no-build : 이미지를 빌드하지 않음
    * -t, —timeout : 타임아웃 시간 지정

* 여러 컨테이너 확인 (ps/logs)

  ~~~
  docker-compose ps
  docker-compose logs
  ~~~

* 여러 컨테이너 구동, 중지, 재가동(start, stop, restart)

  ~~~
  docker-compose start
  docker-compose stop
  docker-compose restart
  ~~~

  * 특정 컨테이너만 조작하고 싶을 경우

    ~~~
    docker-compose restart <특정컨테이너>
    ~~~

    

* 컨테이너 강제 종료

  * SIGINT : 키보드에서 ctrl+c 입력한 것과 같은 결과
  * SIGINT 옵션이 없다면 프로세스를 강제 종료하는 SIGKILL을 보냄

  ~~~
  docker-compose kill -s SIGINT
  ~~~

  
