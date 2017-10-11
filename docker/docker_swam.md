# docker swarm

* Docker swarm은 docker엔진의 클러스터를 만들고 관리하는 기술.
* 노드에서 배포된 서비스는 같은 클러스터내 다른 노드에서 접근 가능



# docker swarm 특징

* 서비스의 가용성 높임 (high availability)
* auto load-balancing
* 분산된 접근
* Scale-up 배포 쉬움



# Docker swram for High availablity

~~~
[Docker Swarm Cluster]
    MANAGER
 Node1, Node2  <-> Client
~~~



[터미널1 - 매니저]

 Docker swarm init —advertise-addr 192.168.1.100

 토큰 생기면 이걸 복사 (docker swarm join로 시작하는것)



[터미널2 - 노드1]

다른 터미널(다른서버)

복사한 토큰을 붙여넣고 실행



[터미널3 - 노드2]

터미널2와 동일하게 실행해서 노드 생성



실행후, 터미널 1에서 docker node ls로 이미지 확인
