# online_images_collector
一个在线的图片采集器，复制链接，一键批量下载想要的图片

# 启动方式
## 源码下载
### github方式
```
# HTTPS
git clone https://github.com/Eternal134/online_images_collector.git
# SSH
git clone git@github.com:Eternal134/online_images_collector.git
```

## 环境准备
### 编译环境
#### Python3.7
下载链接：<a href='https://www.python.org/downloads/'>Python下载</a>
#### JDK11
下载链接：<a href='https://www.oracle.com/cn/java/technologies/javase/jdk11-archive-downloads.html'>JDK下载</a>
#### Node.js
下载链接：<a href='https://nodejs.org/en/download/'>Node.js下载</a>

### 运行工具
#### Docker和docker-compose
下载地址：<a href='https://www.docker.com/get-started/'>Docker下载</a>

## 启动步骤
### 在server文件夹下创建Python虚拟环境
打开命令行，输入以下指令创建虚拟环境：
```
virtualenv venv --python=python3.7
```
激活虚拟环境：
```
# unix
source venv/bin/activate
# win
venv\Scripts\activate
```
在虚拟环境中一键下载Python依赖：
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir
```
### 使用Docker容器启动后端服务
在当前目录下打开命令行，输入docker-compose指令启动docker容器：
```
docker compose up -d
```
### 启动前端项目
使用JS编译器打开client文件夹，启动Vue.js项目

## 访问服务
在浏览器中访问地址localhost:8080即可访问本项目