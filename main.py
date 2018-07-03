import numpy as np
import sys
from readtable import Data
import pandas as pd

'''Call the class to read the input table and store information'''

data1 = Data(sys.argv[1])
data = data1.read()

print data['Hoja2'].columns
print data['Hoja2'].Sex
