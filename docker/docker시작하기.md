* docker 버전 확인

~~~
docker -version
docker-compose -version
~~~



* docker 상태 표시

  ~~~
  docker ps		# 살아있는 프로세스 도커 컨테이너 이미지만 보여줌
  docker ps -a    # 살아있는 프로세스 도커 컨테이너 및 중단되어 있는 이미지 모두 보여줌
  ~~~

  

* docker 이미지 확인

  ~~~
  docker images
  ~~~



* 컨테이너에서 이미지를 사용할 수 있음.



* 도커 이미지는 어디에서 구할까? Docker hub에서 구하면 됨



* 도커는 리눅스 컨테이너 기반이므로, 대부분의 이미지가 리눅스 기반임.



# docker with nginx 예제

* 도커 이미지 가져오기

  ~~~
  docker pull nginx:버전명

  docker images # 이미지 확인
  ➜  docker images
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  nginx               latest              da5939581ac8        3 weeks ago         108MB
  ~~~



* 컨테이너 시작

  ~~~
  docker run --name my-nginx -p 80:80 nginx

  # --name : docker 컨테이너 이름 (여기 예제에서는 my-nginx라고 설정)
  # -p : 포트지정 (docker 80포트는 내 로컬에 80포트에 매핑)
  # 맨뒤에 nginx:버전이름 이런식으로 버전 사용 가능

  # -d 옵션 : 데몬으로 실행가능 (예:docker run --name my-nginx -d -p 80:80 nginx)
  ~~~



* 확인 (웹브라우저) : Welcome to nginx! 확인할 수 있음

  ~~~
  http://localhost:80
  ~~~



* 도커 이미지 내에 있지만, 실제 파일리스트에서 명령어 치는 것과 비슷함.

  ~~~
  docker exec -ti my-nginx /bin/sh
  # ls -al <-입력해보기 (리스트 나옴)
  # cat /etc/nginx/nginx.conf
  (아래 나오는 설정파일 복사해서 텍스트 에디터에 넣기)


  (ref) exec : 실행하라는 명령어
  (ref) -ti : 내부적으로
  ~~~



* 에디터에서 복사한 텍스트에서 gzip on쪽에 주석 풀고 저장(여기 예제에서는 /Users/dev 하위폴더에 저장해봤음)

  ~~~
  user  nginx;
  worker_processes  1;

  error_log  /var/log/nginx/error.log warn;
  pid        /var/run/nginx.pid;


  events {
      worker_connections  1024;
  }


  http {
      include       /etc/nginx/mime.types;
      default_type  application/octet-stream;

      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

      access_log  /var/log/nginx/access.log  main;

      sendfile        on;
      #tcp_nopush     on;

      keepalive_timeout  65;

      gzip  on;

      include /etc/nginx/conf.d/*.conf;
  }
  ~~~



* 터미널로 돌아옴

  * -v 옵션 : A에서 B로 마운트 하라는 옵션
    * /Users/dev/nginx.conf(로컬) 과 /etc/nginx/nginx.conf(도커 컨테이너 내) 를 바인딩
  * ro : read only

  ~~~
  docker run --name my-nginx -d -v /Users/dev/nginx.conf:/etc/nginx/nginx.conf:ro -p 80:80 nginx
  ~~~

  * 실행결과 : localhost:80에서 확인시
    * 크롬 개발자 도구에서 Network 탭에서 Response header 확인해보면, content-encoding:gzip으로 바뀜



* 간단한 index.html 파일 하나 생성 후(/Users/dev/src), 아래 명령어 실행

  ~~~
  <h1>Hello, World</h1>
  ~~~

  * /Users/dev/src (로컬)와 /usr/share/nginx/html(도커 컨테이너 내) 폴더 바인딩

    ~~~
    dev docker run --name my-nginx -d -v /Users/dev/nginx.conf:/etc/nginx/nginx.conf:ro -v /Users/dev/src:/usr/share/nginx/html:ro -p 80:80 nginx
    ~~~

  * 브라우저에서 Hello, World 확인 가능 (서버 재시작 없이, html 로컬에서 바꿀때 바로 반영가능)

  

- 도커 컨터이너 중단

  ~~~
  docker stop my-nginx
  ~~~

  

* 이미지 삭제

  ~~~
  docker rm my-nginx
  ~~~



