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

## 4. models 模版
```python
import utils
import setting
import warnings
import logging
import torch
from typing import *

torch.backends.cudnn.deterministic = True

warnings.filterwarnings('ignore')

config = setting.Config(data_name='chip_ev3',
                        model_name='basic_bert',
                        bs=64,
                        embedding_dim=768,
                        cuda_device=0 if torch.cuda.is_available() else -1,
                        pretrained_model='bert-base-chinese'
                        )

_log_file = utils.generate_time_file(config.log_path, 'log')
logging.basicConfig(
        handlers=[
            logging.FileHandler(
                    filename=_log_file,
                    mode='w',
                    encoding='utf8'),
        ],
        level=logging.DEBUG
)
#...
#...
def train():
    #...
    utils.sent_email(_log_file, 'fscore')
if __name__ == '__main__':
    train()
```
