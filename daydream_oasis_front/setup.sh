
# 杀死旧进程
kill -9 $(lsof -i:81)
wait

# 安装依赖库
#npm install
#wait

# 打包
npm run docs:build
wait

# 启动评论系统
kill -9 $(lsof -i:6870)
# 写入discuss的配置文件
echo "
# Discuss environment Config
# 启动的端口号(仅对服务器有用)
DISCUSS_PORT=6870
# Token 加密的密钥字符串([可选]自定义)
DISCUSS_SECRET=discuss
# 设置评论是否开启审核模式
DISCUSS_AUDIT=false
## 可选数据库 [mongodb, mysql, postgresql, sqlite, cloudbase]
DISCUSS_DB_TYPE=mysql
# ------ MySQL ------
D_MYSQL_URL=mysql://$db_USER:$db_PASSWORD@db_HOST:$db_PORT/$db_NAME
# 例子: mysql://username:password@host:port/database
" > .env
nohup node docs/discuss/index.cjs > setup.log &

# 启动
nohup npm run docs:preview > setup.log &
