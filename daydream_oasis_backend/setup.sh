
#杀死旧的uwsgi
kill -9 $(lsof -i:6666)

#启动新的uwsgi
source venv/bin/activate
uwsgi uwsgi.ini

#重载nginx
nginx -s reload
