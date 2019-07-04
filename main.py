""" ========== Genetic Aplications: Table Adapter (GA:TA) =========

$Id: main.py
$created: Jul 2018
$auth(alphabetical order): del Palacio, S.; Di Santo, P.; Gamboa Lerena, M. M.
$license: GPLv3 or later, see https://www.gnu.org/licenses/gpl-3.0.txt

          This is free software: you are free to change and
          redistribute it.  There is NO WARRANTY, to the extent
          permitted by law.

Contact: unlpbiotec@gmail.com
Technical contact: mgamboa@fcaglp.unlp.edu.ar

This software was developed thanks to finantial support from CONICET (Argentina)

Thanks to Federico Lopez Armengol for helping us with the meta structure and Github usage

Latest upload: July 2019

"""

# Load general modules
import sys
import os
import numpy as np
import pandas as pd

# Load specific modules
from readtable import Data
from R_structure import R
from Arlequin_structure import Arlequin
from Structure_structure import Structure

"""Call the class to read the input table and store information"""

# Condition that no argument equals to producing all outputs (currently 3 tables)
if len(sys.argv) == 3:
	argum = set(sys.argv[1].lower())
	data = Data(sys.argv[2])
else:
	argum = 'ras'
	data = Data(sys.argv[1]) 

# Verbose. data.info parameter is defined in Parameters() method in readtable module
if data.info:
	print '{0} file contains {1} individuals: {2} women and {3} men.'.format(
	sys.argv[2], data.total_MenWomen, data.n_women, data.n_men)
	print 'The sheet has {0} subpopulations, each one with {1} individuals'.format(data.totalPopulations, data.n_each_population)
	print 'Number of markers: {0}. Marker names: {1}'.format(data.n_markers, data.markers)
	#print np.shape(data.markers)
	print 'Women per subpopulation', data.women4subpop

	print 'Men per subpopulation', data.men4subpop

	print 'Filevalues dimensions', np.shape(data.fileValues)

if 'r' in argum:
	R(data)

if 'a' in argum: 
	Arlequin(data)

if 's' in argum:
	Structure(data)

