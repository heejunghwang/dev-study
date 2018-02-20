# Nginx 설치

* Ubuntu 기준

~~~
$ sudo apt-get update
$ sudo apt-get install nginx
$ nginx -v
nginx version: nginx/1.10.3 (Ubuntu)
~~~


# Nginx 사용

## 시작
~~~
$ sudo systemctl start nginx
~~~

## 중지
~~~
$ sudo systemctl stop nginx
~~~

## 재시작
~~~
$ service nginx restart
~~~

# Nginx 설정
* vim file create
~~~
sudo vim /etc/nginx/sites-avaliable/PROJECT_NAME
server {
    listen 80;
    server_name _;

	location / {
			root   /PROJECT_DIRECTORY;
			index  index.html index.htm;
	}

}
~~~

* 이렇게 `sites-available`에 생성해준 파일을 `sites-enabled`에 심볼릭 링크로 파일을 생성
~~~
sudo ln -s /etc/nginx/sites-available/PROJECT_NAME /etc/nginx/sites-enabled/
~~~

* default 디렉토리를 삭제해줘야 configtest가 제대로 나옵니다
~~~
$ sudo service nginx configtest
~~~

~~~
sudo service nginx restart
~~~

* Vue-cli build
~~~
npm run build
~~~

* 빌드 후 `/dist` 하위 폴더 `/PROJECT_DIRECTORY`로 복사

ref) http://blog.leop0ld.org/posts/use-python3-django-uwsgi-nginx/

