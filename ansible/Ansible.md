# 1. Ansible의 기본

## Ansible 이란

* Python으로 구현된 오픈소스 IT 자동화 도구
* 서버 설정, 미들웨어 설치, 소프트웨어 배포, 복수의 호스트를 자동화 구성 관리 도구
* 최근 Ansible 버전 : 2.4 (2018년 3월 4일 기준)



## Ansible 특징

* Agent-less
  * 클라이언트 프로그램을 호스트에 설치할 필요 없음 (예: Chef, Puppet)
  * SSH 접속 가능한 호스트라면 대부분 Ansible로 태스크 실행 가능


* 이해하기 쉬움
  * 실행태스크를 Playbook이라는 YAML 형식으로 기술
  * YAML 로 실행 태스크를 작성하기만 하면 되므로 복잡한 구문을 기억할 필요가 없다.
* 다양한 모듈
  * 다양한 태스크를 실행하기 위해 수많은 모듈이 마련되어 있음
* 멱등성(idempotence)
  * 같은 조작을 몇번이고 수행하더라도 같은 결과가 얻어지는 성실
* 애드혹(Ad-hoc) 명령
  * ansible 명령이라는 단일 모듈만을 실행하는 명령이 있음
  * Playbook을 작성하지 않더라도 ansible 명령을 터미널에서 실행하는 것만으로도 모듈 실행 가능



## Ansible 이용 환경

* Ansible 명령을 실행하는 **실행 호스트**와 태스크를 실행하는 **대상 호스트**가 있음
* Ansible 설치할 필요가 없고, Python 2.4이상 설치되어야함. (Python 3이상은 미리보기 지원)




(참고) 앤서블을 가동하기 위한 요건

* 리눅스/유닉스 계열의 OS환경
* 윈도우 : 윈도우 환경에서는 앤서블 사용할 수 없음
  * 리눅스 가상 머신 사용
  * Windows Subsystem for Linux의 우분투 환경 사용
  * Cygwin은 지원 하지 않음.
* 파이썬 3은? (2018년 3월기준)
  * 파이썬 3 대응은 늦어지고 있는 상태임.
  * 아마 곧..?



## 실행환경

* VirtualBox

  * https://www.virtualbox.org/wiki/Downloads
  * 맥OS 설치 제대로 안될 경우 : http://blog.weirdx.io/post/50287

* Vagrant

  * 설치

  * 설치 후 설정파일 자동으로 만들기

    ~~~
    ➜  devops vagrant init bento/centos-7.2

    A `Vagrantfile` has been placed in this directory. You are now
    ready to `vagrant up` your first virtual environment! Please read
    the comments in the Vagrantfile as well as documentation on
    `vagrantup.com` for more information on using Vagrant.
    ~~~

  * VM 가동

    ~~~
    vagrant up
    ~~~

  * SSH 로그인을 위한 설정정보 `ssh-config` 명령어로 확인 가능

    * HostName, User, Port, IdentityFile은 SSH 접속에 필요한 정보임.

    ~~~
    ➜  devops vagrant ssh-config
    Host default
      HostName 127.0.0.1
      User vagrant
      Port 2222
      UserKnownHostsFile /dev/null
      StrictHostKeyChecking no
      PasswordAuthentication no
      IdentityFile /Users/hwang/dev/devops/.vagrant/machines/default/virtualbox/private_key
      IdentitiesOnly yes
      LogLevel FATAL
    ~~~

  * VM 접속

    * ssh로도 접속 가능하다

    ~~~
    ➜  devops vagrant ssh       
    [vagrant@localhost ~]$ 
    ~~~

    



## Ansible 설치

* Yum, apt-get, pip 등으로 설치 가능.

~~~
brew install ansible
~~~

* 버전확인 : `ansible —version`

~~~
➜  devops ansible --version

ansible 2.4.3.0
  config file = None
  configured module search path = [u'/Users/hwang/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/Cellar/ansible/2.4.3.0_3/libexec/lib/python2.7/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 2.7.14 (default, Mar  9 2018, 23:57:12) [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)]
~~~



## ansible.cfg

* Ansible에 관해 설정하는 INI 파일
* 참조 파일 경로 변경, 환경변수 설정, 명령 동작 변경 등 가능
* 이 책에서는 디폴트로만 설정, 자세한것은 공식 매뉴얼 참고



## 인벤토리

* `ansible`, `ansible-playbook` 명령으로 테스크의 실행 대상 호스트의 정보를 기술하는 텍스트 파일

* 예)

  ~~~
  192.168.34.21 ansible_ssh_user=vagrant ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key
  ~~~

* 주요 접속 정보

  * ansible_ssh_host : 대상 호스트
  * ansible_ssh_port : SSH 접속 포트
  * ansible_ssh_user : SSH 사용자명
  * ansible_ssh_private_key_file : 공개키 인증 비밀키 파일
  * ansible_ssh_pass : 패스워드인증 시 패스워드
