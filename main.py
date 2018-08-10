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
print 'Number of markers: {0} and are: {1}'.format(data.n_markers, data.markers)
print np.shape(data.markers)
print 'Women per subpop', data.women4subpop

print 'Mens per subpop', data.men4subpop

print 'filevalues shape', np.shape(data.fileValues)

# Tomamos la subpoblacion 1:
subpop1_w = data.women4subpop
subpop1_m = data.men4subpop
# Los marcadores son: data.markers

marker_mod = []
for each in data.markers:
	marker_mod.append(str(each)+'A')
	marker_mod.append(str(each)+'B')

print '======================================='
print 'data.populations shape', np.shape(data.populations)
#print data.populations[3]

# Modifico women:
#data_women = []
#for each in data.


#print 'Now. Mens and Women are new class... So each men and women is an object.'
#print 'The format of Mens are:'
#print 'The format of Women are:'