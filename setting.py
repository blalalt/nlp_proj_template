import os
import sys
import utils
from collections import UserDict


def _get_base_dir():
    this_path = os.path.abspath(__file__)
    _prefix = os.path.split(this_path)[0]
    return _prefix


base_dir = _get_base_dir()
sys.path.append(base_dir)


class Config(UserDict):
    def __init__(self,
                 data_name,
                 model_name,
                 bs=128,
                 epoch=100,
                 lr=0.0001,
                 cuda_device=-1,
                 threshold=0.5,
                 max_seq_len=510,
                 embedding_dim=None,
                 pretrained_model=None,
                 **kwargs
                 ):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.max_seq_len = max_seq_len
        self.threshold = threshold

        self.base_dir = base_dir

        self.data_home = utils.get_abs_path(self.base_dir, 'data')
        self.data_path = utils.get_abs_path(self.data_home, data_name)
        self.cache_data = utils.get_abs_path(self.data_path, 'Instance')

        self.log_home = utils.get_abs_path(self.base_dir, 'log')
        log_path = utils.get_abs_path(self.log_home, data_name)
        self.log_path = utils.get_abs_path(log_path, model_name)
        utils.re_mkdir(self.log_path)

        self.epoch = epoch
        self.learning_rate = lr
        self.batch_size = bs
        self.cuda_device = cuda_device

        self.pretrained_model = pretrained_model

        self.rnn_hidden_size = 200

        self.random_state = 914

        self.update(kwargs)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
