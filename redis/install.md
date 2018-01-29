# redis 설치

### version : 4.0.7

## 1. redis 홈페이지에서 다운로드  후 압축 풀어준다

## 2. Prerequirement
* tcl 설치
~~~
apt-get install tcl
yum install tcl
~~~

## 3. redis 폴더에서 make 실행
~~~
[test@localhost redis-4.0.7]$ make
[test@localhost redis-4.0.7]$ make test
~~~


## 4. PREFIX 지정
~~~
[test@localhost redis-4.0.7]$ make PREFIX=/usr/local/redis-4.0.7
[test@localhost redis-4.0.7]$ make test
~~~


## 5. utils 하위 디렉토리의 설치 쉘 실행
* root 권한으로 설치 필요
~~~
[test@localhost redis-4.0.7]$ cd utils/
[test@localhost utils]$ sudo ./install_server.sh
~~~

* (참고) 기본 포트는 6379

* 설치 시 아래 메시지 나타날 때
  * Mmmmm...  it seems like you don't have a redis executable. Did you run make install yet?
~~~
[root@localhost utils]# sudo ./install_server.sh
Welcome to the redis service installer
This script will help you easily set up a running redis server


Please select the redis port for this instance: [6379]
Selecting default: 6379
Please select the redis config file name [/etc/redis/6379.conf]
Selected default - /etc/redis/6379.conf
Please select the redis log file name [/var/log/redis_6379.log]
Selected default - /var/log/redis_6379.log
Please select the data directory for this instance [/var/lib/redis/6379]
Selected default - /var/lib/redis/6379
Please select the redis executable path []
Mmmmm...  it seems like you don't have a redis executable. Did you run make install yet?

~~~

  * 이 경우, executable path에 압축을 푼 redis-4.0.7하위 폴더 하위의 bin/redis-server 경로를 써준다
    * 예) `SOMEWHERE/redis-4.0.7/bin/redis-server`

* (참고 링크) https://www.manniwood.com/redis_30_compile_install_howto/index.html


## 6. 설치 확인
~~~
[root@localhost bin]# ./redis-cli
127.0.0.1:6379> ping
PONG
~~~


## 7. 비밀번호 설정
~~~
$ vi /etc/redis/6379.conf
~~~

* 주석을 푼 후에, 사용자 패스워드 설정
~~~
requirepass userpassword
~~~


* 설정 후 재시작
~~~
$ /etc/init.d/redis_6379 stop 

$ /etc/init.d/redis_6379 start 
~~~

## 8. 확인
* `./redis-cli`에서 `ping` 입력하면, 아래와 같이 메시지 변경됨
~~~
127.0.0.1:6379> ping
(error) NOAUTH Authentication required.
~~~

* `auth 사용자패스워드` 를 입력하면 제대로 접속이 됨
~~~
127.0.0.1:6379> auth userpassword
OK
~~~

* 또는 옵션 `-a 패스워드`를 입력한다
~~~
$ ./redis-cli -a userpassword
127.0.0.1:6379> ping
PONG
~~~

# (참고) 외부 접속 허용
* config 파일(설치 시 설정하였던)에서 bind 부분 주석 제거
* redis 서비스 재시작
~~~
$ cd /etc/redis
$ vi 6379.conf

(conf 파일에서 아래부분 주석처리)
# bind 127.0.0.1
~~~


