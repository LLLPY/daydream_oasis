#切换到虚拟环境
source ../venv/bin/activate

#启动uwsgi
kill -9 $(lsof -i:6666)
uwsgi uwsgi.ini

#重载nginx
service nginx reload