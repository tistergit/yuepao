# 二开推荐阅读[如何提高项目构建效率](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/scene/build/speed.html)
# 选择基础镜像。如需更换，请到[dockerhub官方仓库](https://hub.docker.com/_/python?tab=tags)自行选择后替换。
# 已知alpine镜像与pytorch有兼容性问题会导致构建失败，如需使用pytorch请务必按需更换基础镜像。
FROM ubuntu:latest

# FROM python:3

# # 容器默认时区为UTC，如需使用上海时间请启用以下时区设置命令
# RUN apt-get update && apt-get -y install tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone
RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list \
  && sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list \
  && apt-get -y update 
# && apt-get -y upgrade



ENV TZ=Asia/Shanghai
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

# 使用 HTTPS 协议访问容器云调用证书安装
RUN apt-get -y install ca-certificates
# 安装依赖包，如需其他依赖包，请到alpine依赖包管理(https://pkgs.alpinelinux.org/packages?name=php8*imagick*&branch=v3.13)查找。
# 选用国内镜像源以提高下载速度
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tencent.com/g' /etc/apk/repositories \
# 安装python3
RUN apt-get -y  install wget libgl1 libglib2.0-0 python3 python3-pip 

RUN wget -q -O /tmp/libssl1.deb http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb \
  && dpkg -i /tmp/libssl1.deb \
  && rm /tmp/libssl1.deb \
  && rm -rf /var/cache/apt/*

# 拷贝当前项目到/app目录下（.dockerignore中文件除外）
COPY ./miniapp /app
COPY requirements.txt /app/requirements.txt

# 设定当前的工作目录
WORKDIR /app

# 安装依赖到指定的/install文件夹
# 选用国内镜像源以提高下载速度
RUN --mount=type=cache,target=/root/.cache/pip \
  pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
  && pip config set global.trusted-host mirrors.cloud.tencent.com \
  && pip install --upgrade pip \
  # pip install scipy 等数学包失败，可使用 apk add py3-scipy 进行， 参考安装 https://pkgs.alpinelinux.org/packages?name=py3-scipy&branch=v3.13
  && pip install --user -r /app/requirements.txt


# 执行启动命令
# 写多行独立的CMD命令是错误写法！只有最后一行CMD命令会被执行，之前的都会被忽略，导致业务报错。
# 请参考[Docker官方文档之CMD命令](https://docs.docker.com/engine/reference/builder/#cmd)
# CMD ["uvicorn", "main:create_app"]
# CMD ["/bin/python3", "-m",  "uvicorn", "main:create_app","--host", "0.0.0.0" , "--port", "8000"]
