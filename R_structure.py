import numpy as np
import pandas as pd

class R():

	''' R structure. It returns mens and womens format for R.'''

	def __init__(self, Data):

		if not Data:
			raise ValueError('you must to specify where the Data is.')

		# Tomamos la subpoblacion 1:
		subpop1_w = Data.women4subpop
		subpop1_m = Data.men4subpop
		
		self.womens = []
		self.mens = []

		# Define R markers type
		self.marker_mod = []
		# The first two columns are indivudual number (reset for each subpopulation) and population number, then markers.
		self.marker_mod.append(str('IND'))
		self.marker_mod.append(str('POP'))
		for each in Data.markers:
			self.marker_mod.append(str(each).strip()+'A')
			self.marker_mod.append(str(each).strip()+'B')

		for each_pop in Data.populations:
			auxPop = self.RType(Data, each_pop)
			self.womens.append(auxPop[0])
			self.mens.append(auxPop[1]) 

		self.data = []
		for i in range(len(self.womens)):
			self.data.append(np.concatenate((self.womens[i], self.mens[i]), axis = 0) ) 

		self.data = np.concatenate(self.data, axis = 0)
		self.header = ''
		for i in self.marker_mod:
			self.header = self.header + '{:7s}\t'.format(i)

		
	def RType(self, Data, pop):
		# Modifico women and mens:

		poblacion = pop 
		poblacion_w = []
		poblacion_m = []

		for each in poblacion:
			if each[1] == 2:
				poblacion_w.append(each)
			elif each[1] == 1:
				poblacion_m.append(each)
	 
		markersWom_forR = np.empty((len(poblacion_w)/2,len(self.marker_mod)), dtype = np.int8)
	
		for i in range(0,len(poblacion_w),2):
			markersWom_forR[i/2,0] = int(poblacion_w[i][0]) # First column == individual number
			markersWom_forR[i/2,1] = int(poblacion_w[i][2]) # Second column == population number
			for j in range(0, 2*len(Data.markers), 2):
					j+=1
					markersWom_forR[i/2,j+1] = int(poblacion_w[i][3+j/2])
					markersWom_forR[i/2,j+2] = int(poblacion_w[i+1][3+j/2])
		
		# Mens. Remember odd and even

		if len(poblacion_m)%2 == 0:
			pass
		elif len(poblacion_m)%2 == 1:
			# tengo que generalizarlo por si no es -9 el marcador que hace referencia a MissingData
			poblacion_m.append([-9 for x in range(np.shape(poblacion_m)[1])])

		markersMen_forR = np.empty((len(poblacion_m)/2,len(self.marker_mod)), dtype = np.int8)

		k = len(markersWom_forR)
		for i in range(0,len(poblacion_m),2):
			k += 1
			markersMen_forR[i/2,0] = int(k)	# First column == individual number
			markersMen_forR[i/2,1] = int(poblacion_m[i][2])	# Second column == population number
			for j in range(0, 2*len(Data.markers),2):
				j+=1
				markersMen_forR[i/2,j+1] = int(poblacion_m[i][3+j/2])
				markersMen_forR[i/2,j+2] = int(poblacion_m[i+1][3+j/2])
		
		return markersWom_forR, markersMen_forR






