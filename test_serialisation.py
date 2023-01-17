from dataclasses import dataclass
import pickle
from typing import Tuple

from alts.modules.oracle.data_source import GaussianProcessDataSource
import GPy
import numpy as np

#gp = GaussianProcessDataSource(kern = GPy.kern.Brownian())()

@dataclass
class Test:
    kern: GPy.kern.Brownian = GPy.kern.Brownian()

test = Test(GPy.kern.Brownian())

bytes = pickle.dumps(test)


obj = pickle.loads(bytes)
print(obj)