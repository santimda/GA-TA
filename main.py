import numpy as np
import sys
from readtable import Data
from R_structure import R
import pandas as pd

'''Call the class to read the input table and store information'''
#read the table and return a data with many atributes

data = Data(sys.argv[1])

print '{0} file contains: {1} total number of persons in study, with {2} womens and {3} mens.'.format(
	sys.argv[1], data.total_MenWomen, data.n_women, data.n_men)
print 'The investigation has {0} subpopulations with: {1} persons each one'.format(data.totalPopulations, data.n_each_population)
print 'Number of markers: {0} and are: {1}'.format(data.n_markers, data.markers)
print np.shape(data.markers)
print 'Women per subpop', data.women4subpop

print 'Mens per subpop', data.men4subpop

print 'filevalues shape', np.shape(data.fileValues)

# Invoco a R

#print data.populations[2]

rdata = R(data)
np.savetxt('outputR.txt', rdata.dat, fmt='%4d', header = rdata.header)

