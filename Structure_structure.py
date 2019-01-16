import numpy as np
import pandas as pd

class Structure():

	''' Structure structure (forgive the redundancy). It returns mens and womens format for Structure.'''

	def __init__(self, Data):

		if not Data:
			raise ValueError('you must to specify where Data is.')

		# Tomamos la subpoblacion 1:
		subpop1_w = Data.women4subpop
		subpop1_m = Data.men4subpop
		
		self.womens = []
		self.mens = []

		# Define Estructure markers type
		self.marker_mod = []
		# The first column is population number, then markers.
		self.marker_mod.append(str('POP'))
		for each in Data.markers:
			self.marker_mod.append(str(each).strip())

		# self.header is only for safer programming, but it will not be in output file
		self.header = ''
		for i in self.marker_mod:
			self.header = self.header + '{:7s}\t'.format(i)

		for i, each_pop in enumerate(Data.populations):
			auxPop = self.StructureType(Data, each_pop, i)
			self.womens.append(auxPop[0])
			self.mens.append(auxPop[1]) 

		self.data = []
		for i in range(len(self.womens)):
			self.data.append(np.concatenate((self.womens[i], self.mens[i]), axis = 0) ) 

		self.data = np.concatenate(self.data, axis = 0)

		#Save data to a file
		self.Output(Data)

	def Output(self, Data):
		#Save data to a file
		OutputStrDF = pd.DataFrame(self.data)
		Writer = pd.ExcelWriter(Data.outputNameStr + Data.outputExtensionFile)
		OutputStrDF.to_excel(Writer, sheet_name = 'Sheet1', na_rep = ' ', index = False, header = False)
		Writer.save()

	def StructureType(self, Data, pop, l):

		'''In this structure, womens keep the same shape. Mens are fake womens with a -9 row and add a third row for each individual 
		with a weight (0.5 for womens 1.0 for mens) 
		This method work over one populations. __init__() interprets works with all.

		Parameters:
		
		ColSexType  == column with the 1 or 2 (mens or womens)
		ColPopNum == column with number of population
		ColIndNum == column with number of each individual (or name)
		ColMarkBegin == column where markers starts

		Return: 
		'''

		poblacion = pop
		poblacion_w = []
		poblacion_m = []

		for each in poblacion:
			if each[Data.ColSexType] == Data.IsWomen:
				poblacion_w.append(each)
			elif each[Data.ColSexType] == Data.IsMen:
				poblacion_m.append(each)

		markersWom_forStr = np.empty((len(poblacion_w)+Data.women4subpop[l],len(self.marker_mod)), dtype = object)#object)
		markersMen_forStr = np.empty((len(poblacion_m)+2*Data.men4subpop[l],len(self.marker_mod)), dtype = object)#object)

		count_w = 0
		for i in range(0,len(poblacion_w),2):
			
			markersWom_forStr[count_w,0] = int(poblacion_w[i][Data.ColPopNum]) 
			markersWom_forStr[count_w+1,0] = int(poblacion_w[i][Data.ColPopNum])
			markersWom_forStr[count_w+2,0] = ' '#Data.MARKER

			for j in range(1, len(self.marker_mod)):
				markersWom_forStr[count_w,j] = int(poblacion_w[i][j + Data.ColMarkBegin - 1]) #'-1' because range() starts in 1
				markersWom_forStr[count_w+1,j] = int(poblacion_w[i+1][j + Data.ColMarkBegin - 1])
				markersWom_forStr[count_w+2,j] = Data.STRWom #np.full((1,len(Data.n_markers)), 0.5)

			count_w += 3


		count_m = 0
		for i in range(0,len(poblacion_m)):
			
			markersMen_forStr[count_m,0] = int(poblacion_m[i][Data.ColPopNum]) 
			markersMen_forStr[count_m+1,0] = int(poblacion_m[i][Data.ColPopNum])
			markersMen_forStr[count_m+2,0] = ' '#Data.MARKER 

			for j in range(1, len(self.marker_mod)):
				markersMen_forStr[count_m,j] = int(poblacion_m[i][j + Data.ColMarkBegin - 1])
				markersMen_forStr[count_m+1,j] = Data.MARKER
				markersMen_forStr[count_m+2,j] = Data.STRMen #np.full((1,len(Data.n_markers)), 1.0)

			count_m += 3

		return markersWom_forStr, markersMen_forStr






