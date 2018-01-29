# 로그 확인
~~~
tail -n 16 /var/log/redis_6379.log
~~~

# master-slave 설정
* 여기 예제에서는 다른 포트로 실행 (예: slave 포트번호 6000번으로 설정)
~~~
$ ./install_server.sh
Welcome to the redis service installer
This script will help you easily set up a running redis server

Please select the redis port for this instance: [6379] 6000
.
.
나머지는 설치과정 동일
~~~


# Slave 설정
* `/etc/redis/6000.conf` (slave 설정정보 위치)
~~~
# slaveof <masterip> <masterport> (마스터 정보)
slaveof 127.0.0.1 6379

# masterauth <master-password> (마스터 비밀번호 설정)
masterauth USERPASSWORD

#주석제거
repl-ping-slave-period 10
repl-timeout 60

~~~
* 설정 후 재시작


# 설정 테스트
* 마스터
~~~
$ redis-cli -p 6379 -a USERPASSWORD
$ keys *
(empty list or set)
$ set test good
OK
$ get test
"good"
~~~

* slave
- slave에서는 읽기만 가능
~~~
$ redis-cli -p 6000 -a USERPASSWORD
$ get test
"good"
$ set test
(error) READONLY You can't write against a read only slave.

$info
..생략
# Replication
role:slave
master_host:127.0.0.1
master_port:6379

~~~

* 참고링크 : http://crystalcube.co.kr/176

# sentinel
* 마스터가 다운되면 자동으로 슬레이브를 마스터로 올려줍니다.
