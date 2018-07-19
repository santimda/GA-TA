import numpy as np
import sys
from readtable import Data
import pandas as pd

'''Call the class to read the input table and store information'''
#read the table and return a data with many atributes
data = Data(sys.argv[1])


print '{0} file contains: {1} total number of persons in study, with {2} womens and {3} mens.'.format(
	sys.argv[1], data.total_MenWomen, data.n_women, data.n_men)
print 'The investigation has {0} subpopulations with: {1} persons each one'.format(data.totalPopulations, data.n_each_population)
print 'Number of markers: {0}'.format(data.n_markers)
