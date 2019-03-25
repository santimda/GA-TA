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
		
		self.women = []
		self.men = []

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
			self.women.append(auxPop[0])
			self.men.append(auxPop[1]) 

		self.data = []
		for i in range(len(self.women)):
			self.data.append(np.concatenate((self.women[i], self.men[i]), axis = 0) ) 

		self.data = np.concatenate(self.data, axis = 0)

		self.men = np.concatenate(self.men, axis = 0)

		self.women = np.concatenate(self.women, axis = 0)
		# Save data to a file
		self.Output(Data)

	def Output(self, Data):

		#Save data to a file

		OutputArlqDF = pd.DataFrame(self.data)
		Writer = pd.ExcelWriter(Data.outputNameArlq + Data.outputExtensionFile)
		OutputArlqDF.to_excel(Writer, sheet_name = 'Sheet1', na_rep = ' ', index = False, header = False)
		Writer.save()

		OutputArlqDFMen = pd.DataFrame(self.men)
		WriterMen = pd.ExcelWriter(Data.outputNameArlq + 'Men' + Data.outputExtensionFile)
		OutputArlqDFMen.to_excel(WriterMen, sheet_name = 'Sheet1', na_rep = ' ', index = False, header = False)
		WriterMen.save()

		OutputArlqDFWomen = pd.DataFrame(self.women)
		WriterWomen = pd.ExcelWriter(Data.outputNameArlq + 'Women' + Data.outputExtensionFile)
		OutputArlqDFWomen.to_excel(WriterWomen, sheet_name = 'Sheet1', na_rep = ' ', index = False, header = False)
		WriterWomen.save()

	def ArlequinType(self, Data, pop):

		'''In this structure, women keep the same format. 
		This method works over one population. __init__() interprets all.
		
		Parameters:
		
		ColSexType  == column with the 1 or 2 (man or woman)
		ColPopNum == column with number of population
		ColIndNum == column with number of each individual
		ColMarkBegin == column where markers start
		ARLQINDEX = 1 , same kind of sex for Arlequin
		MARKER = -9 for missing data

		Return: 

		'''		

		poblacion = pop
		PopName = poblacion[0][Data.ColPopName]
		poblacion_w = []
		poblacion_m = []

		for each in poblacion:
			if each[Data.ColSexType] == Data.IsWoman:
				poblacion_w.append(each)
			elif each[Data.ColSexType] == Data.IsMan:
				poblacion_m.append(each)
		
		# Checks if the male population (=fake women) is odd or even:
		if len(poblacion_m)%2 == 0:
			pass
		elif len(poblacion_m)%2 == 1:
			# Missing data is set to -9 (can be changed if needed)
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




