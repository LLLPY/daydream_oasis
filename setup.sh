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
echo "3.开始启动后端服务..."
cd "$root_path/config" && bash "setup.sh"
echo "4.后端服务启动成功..."

# 2.启动前端服务
echo "7.开始启动前端服务..."
cd "$front_path" && bash "setup.sh" 
echo "8.前端服务启动成功..."

echo "daydream_oasis启动成功!!!"
