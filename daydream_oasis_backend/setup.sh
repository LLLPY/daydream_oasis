
#杀死旧的uwsgi
kill -9 $(lsof -i:6666)
wait
#虚拟环境
if ! [ -d "venv" ]; then
    echo "虚拟环境不存在,开始安装虚拟环境..."
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements_pro.txt
    echo "虚拟环境安装完成..."
fi
wait
source venv/bin/activate
wait
# 启动uwsgi
uwsgi uwsgi.ini
wait
#重载nginx
cp daydream_oasis.conf /etc/nginx/conf.d/daydream_oasis.conf
nginx -s reload
