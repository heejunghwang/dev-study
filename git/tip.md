* 최초 git 저장소에 프로젝트 올릴 때
~~~
cd existing-project
git init
git add --all
git commit -m "Initial Commit"
git remote add origin http://gyahoo617@git.javacafe.ga/scm/luc/lucene-example.git
git push -u origin master
~~~

* 이미 있는 프로젝트에 소스 올릴 때
~~~
cd existing-project
git remote set-url origin http://gyahoo617@git.javacafe.ga/scm/luc/lucene-example.git
git push -u origin master
~~~
