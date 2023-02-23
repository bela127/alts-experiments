import pickle
import copy

import GPy
import numpy as np


min_support = -1
max_support = 1
support_points = 10
query_shape = (1,)
result_shape = (1,)

kern = GPy.kern.Brownian() #use a kernel

rng = np.random.RandomState(None)
support = rng.uniform(min_support, max_support, (support_points, *query_shape))

flat_support = support.reshape((support.shape[0], -1))

results = np.random.normal(0, 1, (1, *result_shape))

flat_results = results.reshape((1, -1))

m = GPy.models.GPRegression(flat_support[:1], flat_results, kern, noise_var=0.0) #use the kernel in a model, so the kernel has a parent


obj = copy.deepcopy(kern) #Now deepcopy the kernel ( now the '_parent_' attribute is set)
print(obj)


bytes = pickle.dumps(kern)


obj = pickle.loads(bytes)
print(obj)