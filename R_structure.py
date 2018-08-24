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
		
		# Define R markers type
		self.marker_mod = []
		for each in Data.markers:
			self.marker_mod.append(str(each).strip()+'A')
			self.marker_mod.append(str(each).strip()+'B')
		
		self.womens = []
		self.mens = []
		for each_pop in Data.populations:
			auxPop = self.R_Type(Data, each_pop)
			self.womens.append(auxPop[0])
			self.mens.append(auxPop[1]) 
		
	def R_Type(self, Data, pop):
		# Modifico women and mens:
		'''Martin (13/08): 	ahora estoy probando con Data.populations[0] que seria la primer subpoblacion, hay que modificarlo
							para hacer lo con todas las que tenga'''

		poblacion = pop # A ser modificado (ver nota)
		poblacion_w = []
		poblacion_m = []

		# La tabla R necesita que la primer columna sea el numero de individue y la segunda columna la poblacion de la que pertenece

		for each in poblacion:
			if each[1] == 2:
				poblacion_w.append(each)
			elif each[1] == 1:
				poblacion_m.append(each)
	
		# The +1 of the shape is because we want a number of populations + markers 
		markersWom_forR = np.empty((len(poblacion_w)/2,len(self.marker_mod)+1), dtype = np.int8)
	
		#print np.shape(poblacion_w), np.shape(markers_forR), np.shape(Data.markers)
	
		for i in range(0,len(poblacion_w),2):
			markersWom_forR[i/2,0] = int(poblacion_w[i][2])
			for j in range(0, 2*len(Data.markers), 2):
					j+=1
					markersWom_forR[i/2,j] = int(poblacion_w[i][3+j/2])
					markersWom_forR[i/2,j+1] = int(poblacion_w[i+1][3+j/2])
		
		# Mens. Remember odd and even

		if len(poblacion_m)%2 == 0:
			pass
		elif len(poblacion_m)%2 == 1:
			# tengo que generalizarlo por si no es -9 el marcador que hace referencia a MissingData
			poblacion_m.append([-9 for x in range(np.shape(poblacion_m)[1])])

		markersMen_forR = np.empty((len(poblacion_m)/2,len(self.marker_mod)+1), dtype = np.int8)
		#print np.shape(poblacion_w), np.shape(markers_forR), np.shape(Data.markers)
	
		for i in range(0,len(poblacion_m),2):
			markersMen_forR[i/2,0] = int(poblacion_m[i][2])
			for j in range(0, 2*len(Data.markers),2):
				j+=1
				markersMen_forR[i/2,j] = int(poblacion_m[i][3+j/2])
				markersMen_forR[i/2,j+1] = int(poblacion_m[i+1][3+j/2])
		
		return markersWom_forR, markersMen_forR






