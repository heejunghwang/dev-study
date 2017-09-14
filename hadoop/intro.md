하둡
scale-out(하드웨어 계속 추가 가능한) 스토리지와 ditriubuted 프로세싱을 제공하는 오픈 소스 데이터 관리 도구

하둡의 2가지 구성
- HDFS : 스토레지 컴포넌트
- YARN : 프로세싱 컴포넌트

1. HDFS (Hadoop Distribued File System)
- Master / Salve 구성
- 각각의 클러스터는 1개의 Namenode(master)와 Datanodes(slave nodes) 가지고 있음
- HDFS에서는 데이터가 block 단위로 저장됨(default는 128MB 정도)

1) Name node
- 메인 메모리에서 메타 데이터를 저장 : 파일 리스트, 파일의 블록 리스트, 데이터 노드의 리스트 등

2) Data nodes
- 실제 데이터가 저장되고 배포되는 곳
- 클라이언트의 요청을 읽고/쓰는 역할을 함

3) secondary node
- name node 백업본

하둡에서의 Replication
- 복사본임, 3개 가지고 있음(카피본이 2개)

rack awareness : 같은 블록에서 저장되는건 아님.

2. YARN (Yet Another Resource Negotiator)
- 클러스터 구성을 이용한 실제 실행하는 컴포넌트
1) Resource Manager(Master)
   - 리소스 관리
2) Node Manager(Slave)
    - 실행되고 컨테이너를 모니터링함
3) Application Master
    - 한개 이상의 컨테이너에서 실행되는 작업
4) Containers
  - 특정 프로세서가 실행됨
