FROM registry.cn-hangzhou.aliyuncs.com/qiumao/online_image_collector:server

# RUN apt-get update && apt-get upgrade -y && apt-get install -y
# 更新pip
RUN python -m pip install --upgrade pip 

WORKDIR /home/server

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir