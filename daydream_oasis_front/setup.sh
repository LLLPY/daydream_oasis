
# 杀死旧进程
kill -9 $(lsof -i:81)

# 启动新的
nohup npm run docs:dev & > daydream_oasis_front.log
