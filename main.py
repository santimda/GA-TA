import numpy as np
import sys
import os
from readtable import Data
from R_structure import R
from Arlequin_structure import Arlequin
import pandas as pd

'''Call the class to read the input table and store information'''
#read the table and return a data with many atributes

argum = sys.argv[1]
argum = set(argum)

data = Data(sys.argv[2])

info = True#False

if info:
	print '{0} file contains: {1} total number of persons in study, with {2} womens and {3} mens.'.format(
	sys.argv[1], data.total_MenWomen, data.n_women, data.n_men)
	print 'The investigation has {0} subpopulations with: {1} persons each one'.format(data.totalPopulations, data.n_each_population)
	print 'Number of markers: {0} and are: {1}'.format(data.n_markers, data.markers)
	print np.shape(data.markers)
	print 'Women per subpop', data.women4subpop

	print 'Mens per subpop', data.men4subpop

	print 'filevalues shape', np.shape(data.fileValues)

# Invoco a R
if 'r' in argum:
	rData = R(data)
	output_name_R = 'outputR'
	np.savetxt(output_name_R+'.txt', rData.data, fmt='%4d', header = rData.header, comments = '')
	# convert .txt in a spreadsheet
	os.system('ssconvert '+output_name_R+'.txt '+output_name_R+'.xlsx')

elif 'a' in argum: 
	arlequinData = Arlequin(data)
	output_name_arlequin = 'outputArlq'
	np.savetxt(output_name_arlequin+'.txt', arlequinData.data, comments = '', fmt='%4d')#, header = arlequinData.header)
	os.system('ssconvert '+output_name_arlequin+'.txt '+output_name_arlequin+'.xlsx')


elif 's' in argum:
	print 's'

else: 
	raise ValueError('You have to specify r (for R), a (for Arlequin) or s (for Structure) parameter.')




