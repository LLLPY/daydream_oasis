### 项目的启动
项目的依赖的基本工具，如python，node.js，uwsgi，nginx，mysql，redis等需要自行进行安装和搭建，这里不做过多的介绍。

#### 1.后端启动
```shell script
# 切换到后端项目的根目录
cd daydream_oasis_backend

# 安装第三方依赖 （开发环境和部署环境二选一即可）
pip install -r config/requirements_dev.txt # 开发环境
pip install -r config/requirements_pro.txt # 部署环境

# 启动项目（根据个人情况选择开发或部署环境启动）
python manage.py runserver #开发环境
uwsgi config/uwsgi.ini # 部署环境
```



#### 2.前端启动

```shell script
# 切换到前端项目的根目录下
cd daydream_oasis_front

# 安装依赖
npm install

#项目启动
npm run docs:dev
```