
# 杀死旧进程
kill -9 $(lsof -i:81)
wait
# 启动新的(日志输出到控制台)
nohup npm run docs:dev > setup.log &
