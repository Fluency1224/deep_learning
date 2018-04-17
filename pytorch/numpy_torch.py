#########################################################################
# File Name: numpy_torch.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 17 Apr 2018 08:09:56 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import numpy as np
import torch

np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)

print('np_data\n', np_data)
print('torch\n', torch_data)
