import numpy as np
import pandas as pd

class Arlequin():

	''' Arlequin structure. It returns mens and womens format for Arlequin.'''

	def __init__(self, Data):

		if not Data:
			raise ValueError('you must to specify where Data is.')

		# Tomamos la subpoblacion 1:
		subpop1_w = Data.women4subpop
		subpop1_m = Data.men4subpop
		
		self.womens = []
		self.mens = []

		# Define Arlequin markers type
		self.marker_mod = []
		# The first two columns are indivudual number (reset for each subpopulation) and population number, then markers.
		self.marker_mod.append(str('IND'))
		self.marker_mod.append(str('POP'))

		for each in Data.markers:
			self.marker_mod.append(str(each).strip())

		# self.header is only for safer programming, but it will not be in output file
		self.header = ''
		for i in self.marker_mod:
			self.header = self.header + '{:7s}\t'.format(i)

		for each_pop in Data.populations:
			auxPop = self.ArlequinType(Data, each_pop)
			self.womens.append(auxPop[0])
			self.mens.append(auxPop[1]) 

		self.data = []
		for i in range(len(self.womens)):
			self.data.append(np.concatenate((self.womens[i], self.mens[i]), axis = 0) ) 

		self.data = np.concatenate(self.data, axis = 0)

		# Save data to a file
		self.Output(Data)

	def Output(self, Data):

		#Save data to a file

		OutputArlqDF = pd.DataFrame(self.data)
		Writer = pd.ExcelWriter(Data.outputNameArlq + Data.outputExtensionFile)
		OutputArlqDF.to_excel(Writer, sheet_name = 'Sheet1', na_rep = ' ', index = False, header = False)
		Writer.save()


	def ArlequinType(self, Data, pop):

		'''In this structure, womens keep the same shape. 
		This method work over one populations. __init__() interprets works with all.
		
		Parameters:
		
		ColSexType  == column with the 1 or 2 (mens or womens)
		ColPopNum == column with number of population
		ColIndNum == column with number of each individual (or name)
		ColMarkBegin == column where markers starts
		ARLQINDEX = 1 #same kind of sex for Arlequin
		MARKER = -9

		Return: 

		'''		

		poblacion = pop
		PopName = poblacion[0][0]
		poblacion_w = []
		poblacion_m = []

		for each in poblacion:
			if each[Data.ColSexType] == Data.IsWomen:
				poblacion_w.append(each)
			elif each[Data.ColSexType] == Data.IsMen:
				poblacion_m.append(each)
		
		# Does man pop (fake womes) odd or even?:
		if len(poblacion_m)%2 == 0:
			pass
		elif len(poblacion_m)%2 == 1:
			# tengo que generalizarlo por si no es -9 el marcador que hace referencia a MissingData
			poblacion_m.append([-9 for x in range(np.shape(poblacion_m)[1])])

		markersWom_forArlq = np.empty((len(poblacion_w),len(self.marker_mod)), dtype = object)#np.int8)
		markersMen_forArlq = np.empty((len(poblacion_m),len(self.marker_mod)), dtype = object)#object)

		for i in range(0,len(poblacion_w),2):
			
			markersWom_forArlq[i,0] = PopName+str(poblacion_w[i][Data.ColIndNum])
			markersWom_forArlq[i,1] = int(Data.ARLQINDEX)
			
			markersWom_forArlq[i+1,0] = ' ' 
			markersWom_forArlq[i+1,1] = ' '
			for j in range(2, len(self.marker_mod)):
				markersWom_forArlq[i,j] = int(poblacion_w[i][j+2])
				markersWom_forArlq[i+1,j] = int(poblacion_w[i+1][j+2])

		count = len(poblacion_w)/2
		
		for i in range(0,len(poblacion_m),2):
			count += 1
			markersMen_forArlq[i,0] = PopName+str(count)
			markersMen_forArlq[i,1] = int(Data.ARLQINDEX)

			markersMen_forArlq[i+1,0] = ' '
			markersMen_forArlq[i+1,1] = ' '
			
			for j in range(2, len(self.marker_mod)):
				markersMen_forArlq[i,j] = int(poblacion_m[i][j+2])
				markersMen_forArlq[i+1,j] = int(poblacion_m[i+1][j+2])

		return markersWom_forArlq, markersMen_forArlq




