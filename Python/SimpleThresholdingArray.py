#from https://stackoverflow.com/questions/32322281/numpy-matrix-binarization-using-only-one-expression

import numpy as np
np.random.seed(0)
np.set_printoptions(precision=3)
a=np.random.rand(4,4)
print a
a=(a>0.5).astype(np.int_)
print a
