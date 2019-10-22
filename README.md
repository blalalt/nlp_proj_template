## 1. 添加当前目录到PYTHONPATH
```shell script
git clone https://github.com/blalalt/nlp_proj_template.git
cd nlp_proj_template
pwd
export PYTHONPATH=当前目录的绝对路径:$PYTHONPATH
```
## 2. 新建其他目录
```shell script
python reset -c
```
会创建 'data', 'log', 'models'三个目录，以及 '.env'文件

## 3. 填写邮箱信息
这是使用的是 163 邮箱，在.env 文件中填写：
```shell script
email=邮箱地址
email_passwd=邮箱密码
```
