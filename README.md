# flaskweb

> 这个库是为了学习《flask web开发》而创建的，使用的PYTHON版本为2.7.12，数据库为mysql，使用前请先安装mysql。

## 将项目克隆到本地

```
# 定位到任意目录
$ cd path/to/root

# 克隆仓库到指定的文件夹
$ git clone git@github.com:Lifeistrange/flaskweb.git

# 进入指定的文件夹
$ cd [project-name]
```

## 环境配置

```
# 安装mysql
sudo apt-get install mysql libmysqlclient-dev

# 创建virtualenv
source env.sh

# 安装对应依赖
pip install -r requirements.txt
```

## 数据库初始化

```
cd domain
python create_db.py
```

## 运行

```
sh run.sh
```
