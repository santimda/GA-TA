import numpy as np
import sys
from readtable import Data
import pandas as pd

'''Call the class to read the input table and store information'''

data1 = Data(sys.argv[1])
colum,values = data1.read()

print values[7]

sys.exit()



columnName = np.array(columnName)
columnValues = np.array(columnValues)


print np.shape(columnName.T), np.shape(columnName[0])

print np.shape(columnValues), np.shape(columnValues[0])

print columnName.T[0], columnValues[0:58]
#print data['Hoja2'].Sex
