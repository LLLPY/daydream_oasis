
# 杀死旧进程
kill -9 $(lsof -i:81)
wait

# 安装依赖库
npm install
wait

# 打包
npm run docs:build
wait

# 启动
nohup npm run docs:preview > setup.log &
