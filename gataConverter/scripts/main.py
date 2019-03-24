""" ========== Genetic Aplications: Table Adapter (GA:TA) =========

This soft ....

Authors (alfabetic order): del Palacio, S.; Di Santo, P.; Gamboa Lerena, M. M.
contact: 

Thanks to Federico Lopez Armengol for help to think the meta structure and for teach us Github (jaja), Fernando.... 

Late upload: January 2019


"""


import sys
import os
import numpy as np
import pandas as pd
from readtable import Data
from R_structure import R
from Arlequin_structure import Arlequin
#from Structure_structure import Structure

'''Call the class to read the input table and store information'''
#read the table and return a data with many atributes

if len(sys.argv) == 3:
	argum = set(sys.argv[1].lower())
	data = Data(sys.argv[2])
else:
	argum = ' '
	data = Data(sys.argv[1]) 

if data.info:
	print ('{0} file contains: {1} total number of persons in study, with {2} womens and {3} mens.'.format(
	sys.argv[1], data.total_MenWomen, data.n_women, data.n_men))
	print ('The investigation has {0} subpopulations with: {1} persons each one'.format(data.totalPopulations, data.n_each_population))
	print ('Number of markers: {0} and are: {1}'.format(data.n_markers, data.markers))
	print (np.shape(data.markers))
	print ('Women per subpop', data.women4subpop)

	print ('Mens per subpop', data.men4subpop)

	print ('filevalues shape', np.shape(data.fileValues))

if 'r' in argum:
	R(data)

if 'a' in argum: 
	Arlequin(data)

#if 's' in argum:
#	Structure(data)

if not 'r' in argum or not 'a' in argum or not 's' in argum: 
	ValueError('You have to specify r (for R), a (for Arlequin) or s (for Structure) parameter.')




