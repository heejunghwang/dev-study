# 앤서블



## 앤서블의 역사

* 미국 레드햇(Red Hat)사가 제공
* 모든 사람을 위한 자동화 를 지향하는 구성 관리 도구



## 엔서블의 구성

* 앤서블
* 인벤터리(inventory) : '어디에서' 앤서블을 실행하는가
* 모듈(module) : '무엇을' 앤서블에서 실행하는가
* 플레이북(playbook) : '어떻게' 앤서블을 실행하는가



## 1. 앤서블

* 힌번 설치하고 난 후에 필요할 때 명령 실행
* 서버/클라이언트 구성과 같은 형태를 취하지 않음



## 2. 인벤터리

* 서버 접속 정보를 표시

~~~
[app]
app1 ansible_host = some.app.host
app2 ansible_host=another.app.host

[db]
db1 ansible_host = db.1.host
db2 ansible_host = db.2.host
~~~





## 3. 모듈

* 앤서블에서 실행된 하나하나의 명령

  * 예) 패키지 설치와 서비스, 파일 복사와 편집, MySQL 과 같은 사용자 테이블 관리, AWS, 애저 서비스 작업 등등
  * 셸 스크립트로 작성하면 복잡한 절차가 필요하지만, 앤서블에 내장된 모듈은 사용자가 의식하지 않고도 안전하고 ㅈ거절한 처리를 실행할 수 있도록 함.

* 내장 모듈 목록은 공식 홈페이지 확인 : http://docs.ansible.com/ansible/devel/modules/modules_by_category.html

* 자주 사용하는 모듈

  * 파일 작업
    * file : 파일 작업
    * copy : 파일을 작성 대상에게 전송
    * lineinfile : 기존 파일을 행 단위로 수정
  * 명령어 실행 모듈
    * command
    * ​

  ​

## 4. 플레이북

* 스크립트(코드)
* 앤서블을 사용할 때 필요한 작업을 플레이북의 구현과 실행이라고 보면됨
* YAML 형식으로 작성됨.



## 앤서블 vs ,피펫, 셰프

### 피펫, 셰프 소개

* 피펫과 셰프는 모두 루비(Ruby)로 구현되어 있음, 앤서블 등장 이전부터 많이 사용됨.
* 피펫 : 독자적인 언어 사용해서 Mainfest 작성해야함
* 셰프 : 루비로 코드 작성 (Recipe라고 함)

## 차이점 

* Agentless

  * 피펫, 셰프의 경우 전용 에이전트가 중앙 서버에 접근해 코드를 가져온 다음, 에이전트 스스로가 해당 머신에 적합한 상태 설정

    * 중앙 서버는 각 머신의 접근 정보를 몰라도 됨

    * 실행 대상 전용 에이전트를 설치해야하는 단점, 에이전트를 도입하기 위한 준비가 필요

    * [셰프의 경우] : pull 형 아키텍쳐

      ![셰프](https://static.wixstatic.com/media/06c82a_e828ad4a86b74bdaa30dec414c876350~mv2.png/v1/fill/w_580,h_256,al_c,lg_1/06c82a_e828ad4a86b74bdaa30dec414c876350~mv2.png)

    * [앤서블의 경우] : push형 아키텍쳐

      ![앤서블](https://d1cg27r99kkbpq.cloudfront.net/static/extra/43-ansible-multi-node-deployment-workflow.png)



## 도커 컴포즈와 vs 앤서블 컨테이너

* 앤서블 컨테이너가 도커 컴포즈 보다 유리한 점
  * 도커 외의 오케스트레이션 환경 문제 해결하는데 적합하지 않음.
  * 도커가 리눅스 배포판에 최적화되어 있다는 점에서 특정 리눅스 배포판에서 도커 컨테이너를 실행시키고 싶을 때는 SE리눅스 활성화가 선행되어야함. 앤서블의 경우 SE리눅스에 대헛 모듈들이 제공되고 있으므로, SE리눅스 context를 쉽게 설정할 수 있음.
  * 앤서블에서 제공되는 수백개의 모듈들은 복잡한 요건을 만족하기 위해서 적합
  * 복잡한 오케스트레이션과 인증, 승인 프로세스를 고려한 워크플로우가 필요한 경우, 앤서블 타워로 프로세스 통합가능
  * 앤서블 2.1 이후 docker_service 모듈을 도커 컴포즈와 호환됨
  * 출처 : https://www.ansible.com/blog/six-ways-ansible-makes-docker-compose-better
