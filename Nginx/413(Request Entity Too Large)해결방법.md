* Error Message
  - When the body request is larger than the default body size
~~~
413 (Request Entity Too Large)
~~~



* Solution
~~~
vi /etc/nginx/nginx.conf
~~~

* set the client body size (if it is more than 2M, you should set more memory)
~~~
# set client body size to 2M #
client_max_body_size 2M;
~~~

* nginx reload
~~~
service nginx reload
~~~
