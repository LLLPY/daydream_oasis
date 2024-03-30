
#杀死旧的uwsgi
kill -9 $(lsof -i:6666)
wait

#虚拟环境
if ! [ -d "venv" ]; then
    echo "虚拟环境不存在,开始安装虚拟环境..."
    python3 -m venv venv
    echo "虚拟环境创建完成..."
fi

# 安装第三方库
pip3 install -r requirements.txt
wait

# 激活虚拟环境
source venv/bin/activate
wait

# 收集静态文件
echo "开始收集静态文件..."
python3 manage.py collectstatic --noinput
echo "静态文件收集完成..."
wait

# 启动uwsgi
uwsgi uwsgi.ini
wait

#重载nginx
cp daydream_oasis.conf /etc/nginx/conf.d/daydream_oasis.conf
# 检查nginx进程是否存在
if pgrep nginx > /dev/null
then
    # nginx进程存在，直接reload配置文件
    nginx -s reload
    echo "Nginx configuration reloaded"
else
    # nginx进程不存在，启动nginx
    nginx
    echo "Nginx started"
fi