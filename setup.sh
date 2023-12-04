#!/bin/bash


project_name="daydream_oasis"
backend_name="${project_name}_backend"
front_name="${project_name}_front"
root_path=$(cd "$(dirname "$0")"; pwd)
backend_path="$root_path/$backend_name"
front_path="$root_path/$front_name"

echo "项目的根目录:$root_path"
echo "后端的根目录:$backend_path"
echo "前端的根目录:$front_path"

# 1.启动后端服务
echo "1.开始启动后端服务..."
cd "$backend_path" && bash "setup.sh" && tail -30 "$backend_path/uwsgi.log"
wait
echo "2.后端服务启动成功..."

# 2.启动前端服务
echo "3.开始启动前端服务..."
cd "$front_path" && bash "setup.sh" && tail -200 "$front_path/setup.log"
wait
echo "4.前端服务启动成功..."

echo "5.$project_name启动成功!!!"
