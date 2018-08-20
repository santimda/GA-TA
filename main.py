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

rdata = R(data)

print np.shape(rdata.mens), np.shape(rdata.womens)
print rdata.womens

header = ''
for i in rdata.marker_mod:
	header = header + '{:7s}\t'.format(i)
dat = np.concatenate((rdata.womens, rdata.mens), axis = 0)

np.savetxt('outputR.txt', dat, fmt='%4d', header = header)























#R_Data_markers.append()
#DataFrame.join()
#DataFrame.merge()
#DataFrame.to_excel()
#						'womens': rdata.womens,
#						'mens': rdata.mens })



#output_file.write('{} /n'.format(rdata.marker_mod))
#for each in rdata.womens:
#	output_file.write('{} /n'.format(each))
#
#for each in rdata.mens:
#	output_file.write('{} /n'.format(each))
#
#output_file.close()