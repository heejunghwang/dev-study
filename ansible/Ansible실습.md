# 앤서블 실습

## 앤서블 설치

~~~
pip2 install ansible
~~~

* 동작확인

~~~
➜ ansible localhost -m ping
 [WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does
not match 'all'

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
~~~



## Virtual Box 준비

## 베이그런트에서 가상머신(VM) 준비하기

* 디렉토리 만들기

~~~
➜  devops mkdir ansible-tutorial
➜  devops cd ansible-tutorial
~~~



* 베이그런트에서 VM을 실행할 수 있게하는 설정파일인 __Vagrantfile__을 생성

  * **vagrant init** 명령으로 생성가능
  * vagrant 공개 이미지는 'https://app.vagrantup.com/boxes/search'에서 찾을 수 있음.

  ~~~
  // Vagrantfile 생성
  ➜  ansible-tutorial : vagrant init bento/centos-7.2

  ==> vagrant: A new version of Vagrant is available: 2.0.3!
  ==> vagrant: To upgrade visit: https://www.vagrantup.com/downloads.html

  A `Vagrantfile` has been placed in this directory. You are now
  ready to `vagrant up` your first virtual environment! Please read
  the comments in the Vagrantfile as well as documentation on
  `vagrantup.com` for more information on using Vagrant.
  ~~~


  // Vagrantfile 생성 확인을 할 수 있다.

~~~~
  ➜  ansible-tutorial ls
    Vagrantfile
~~~~



* Vagrantfile 파일 수정

  * 가상머신->호스트로 접식하기 위한 IP 주소 할당

  * ' config.vm.network' 쪽에 주석 해제

      config.vm.network "private_network", ip: "192.168.33.10"

* VM 기동

  * **vagrant up** 명령어

  ~~~
  ➜  ansible-tutorial vagrant up
  Bringing machine 'default' up with 'virtualbox' provider...
  ==> default: Importing base box 'bento/centos-7.2'...
  ==> default: Matching MAC address for NAT networking...
  ==> default: Checking if box 'bento/centos-7.2' is up to date...
  ==> default: Setting the name of the VM: ansible-tutorial_default_1522073947067_22512
  ==> default: Clearing any previously set network interfaces...
  ==> default: Preparing network interfaces based on configuration...
  ~~~

  ​

## 인벤터리 파일 작성

* 인벤터리

  * 버츄얼박스에 접속하기 위한 정보를 정의한 것
  * 정적/동적 2가지 종류가 있음.
  * 호스트의 목록

  ~~~
  vagrant-machine ansible_host=127.0.0.1 ansible_port=2222 ansible_user=vagrant ansible_ssh_private_key_file=.vagrant/machines/default/virtualbox/private_key
  ~~~



## 설정 파일 만들기



## 접속확인

* ping 모듈을 사용해 접속 확인
  * ansible all -i hosts -m ping

~~~
➜  ansible-tutorial ansible all -i hosts -m ping
vagrant-machine | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
~~~



## 플레이북

* YAML 형식으로 쓰인 시스셈 정의서
* 앤서블에서는 "자동으로 실행된 코드"
* 플레이북 파일 구성
  * ansible-tutorial
    * Vagrantfile
    * hosts
    * site.yml



## 플레이북의 기본형

* 예) site.yml 생성

~~~
---
- name : 플레이북 튜토리얼
  hosts : all
  tasks:
~~~

* 실행
  * tasks 에 아무것도 넣지 않았지만, setup이 됨.

~~~
➜  ansible-tutorial ansible-playbook -i hosts site.yml

PLAY [플레이북 튜토리얼] ********************************************************************************************

TASK [Gathering Facts] **************************************************************************************
ok: [vagrant-machine]

PLAY RECAP **************************************************************************************************
vagrant-machine            : ok=1    changed=0    unreachable=0    failed=0

~~~





* SELinux 대응
  * 수정후, ansible-playbook -i hosts site.yml 실행

~~~
---
- name : 플레이북 튜토리얼
  hosts : all
  become: true
  tasks:
    - name: libselinux-python 설치
      yum:
        name: libselinux-python
        state: present
~~~



* EPEL 리포지터리 설치

~~~
---
- name : 플레이북 튜토리얼
  hosts : all
  become: true
  tasks:
    - name: libselinux-python 설치
      yum:
        name: libselinux-python
        state: present
    - name : EPEL 리포지터리 설치
      yum:
        name: epel-release
        state: present
~~~



* 엔진엑스 설정

~~~
---
- name : 플레이북 튜토리얼
  hosts : all
  become: true
  tasks:
    - name: libselinux-python 설치
      yum:
        name: libselinux-python
        state: present
    - name : EPEL 리포지터리 설치
      yum:
        name: epel-release
        state: present
    - name : 엔진엑스 설치
      yum:
        name: nginx
        state: present
    - name : 엔진엑스 서비스 시작과 자동 시작 설정
      service:
        name: nginx
        state: started
        enabled: true
~~~





* 엔진엑스 확인
  * 브라우저에서 http://192.168.33.10/ 띄우면 엔진엑스가 뜸
