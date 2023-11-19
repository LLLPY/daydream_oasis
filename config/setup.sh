

#切换到虚拟环境
source ../venv/bin/activate

#杀死旧的uwsgi
#kill -9 $(lsof -i:8000)
kill -9 $(lsof -i:6666)

#启动新的uwsgi
uwsgi uwsgi.ini

#重载nginx
systemctl reload nginx
