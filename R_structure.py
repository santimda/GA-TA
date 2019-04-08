import numpy as np
import pandas as pd
import os

class R():

	''' R structure. It returns men and women format for R.'''

	def __init__(self, Data):

		if not Data:
			raise ValueError('Data must be specified')

		# First subpopulation:
		subpop1_w = Data.women4subpop
		subpop1_m = Data.men4subpop
		
		self.women = []
		self.men = []

		# Define R markers type
		self.marker_mod = []
		# The first two columns are individual number (which resets for each subpopulation) and population number. 
		# Next columns are markers.
		self.marker_mod.append(str('IND'))
		self.marker_mod.append(str('POP'))
		for each in Data.markers:
			self.marker_mod.append(str(each).strip()+'A')
			self.marker_mod.append(str(each).strip()+'B')

		for each_pop in Data.populations:
			auxPop = self.RType(Data, each_pop)
			self.women.append(auxPop[0])
			self.men.append(auxPop[1]) 

		self.data = []
		for i in range(len(self.women)):
			self.data.append(np.concatenate((self.women[i], self.men[i]), axis = 0) ) 

		self.data = np.concatenate(self.data, axis = 0)
		self.header = ''
		for i in self.marker_mod:
			self.header = self.header + '{:7s}\t'.format(i)

		#Save data to a file
		self.Output(Data)

	def Output(self, Data):

		# Save data to a file
		np.savetxt(Data.outputNameR+'.txt', self.data, fmt='%4d', header = self.header, comments = '')
		# convert .txt in a spreadsheet
		os.system('ssconvert '+Data.outputNameR+'.txt '+Data.outputNameR+'.xlsx')
		# Remove the temporary .txt file
		os.remove(Data.outputNameR+'.txt')

	def RType(self, Data, pop):
		'''Modify women and men:
		
		Parameters:
		
		ColIndNum == column with number of individual 
		ColSexType == column with 1 or 2 (man or woman)
		ColPopNum == column with number of population

		Return: 

		'''

		#ColIndNum = 1
		#ColSexType = 2
		#ColPopNum = 3
		#ColMarkBegin = 4

		poblacion = pop 
		poblacion_w = []
		poblacion_m = []

		for each in poblacion:
			if each[Data.ColSexType] == Data.IsWoman:
				poblacion_w.append(each)
			elif each[Data.ColSexType] == Data.IsMan:
				poblacion_m.append(each)
	 
		markersWom_forR = np.empty((len(poblacion_w)//2,len(self.marker_mod)), dtype = np.int8)
	
		for i in range(0,len(poblacion_w),2):
			markersWom_forR[i//2,0] = int(poblacion_w[i][Data.ColIndNum]) 
			markersWom_forR[i//2,1] = int(poblacion_w[i][Data.ColPopNum]) 
			for j in range(0, 2*len(Data.markers), 2):
					j+=1
					markersWom_forR[i//2,j+1] = int(poblacion_w[i][Data.ColMarkBegin+j//2])
					markersWom_forR[i//2,j+2] = int(poblacion_w[i+1][Data.ColMarkBegin+j//2])
		
		# Men. Take into account if number of men is odd or even

		if len(poblacion_m)%2 == 0:
			pass
		elif len(poblacion_m)%2 == 1:
			# Missing data is set to -9 (can be changed if needed)
			poblacion_m.append([-9 for x in range(np.shape(poblacion_m)[1])])

		markersMen_forR = np.empty((len(poblacion_m)//2,len(self.marker_mod)), dtype = np.int8)

		k = len(markersWom_forR)
		for i in range(0,len(poblacion_m),2):
			k += 1
			markersMen_forR[i//2,0] = int(k)	# First column (new file)== individual number
			markersMen_forR[i//2,1] = int(poblacion_m[i][Data.ColPopNum])	
			for j in range(0, 2*len(Data.markers),2):
				j+=1
				markersMen_forR[i//2,j+1] = int(poblacion_m[i][Data.ColMarkBegin+j//2])
				markersMen_forR[i//2,j+2] = int(poblacion_m[i+1][Data.ColMarkBegin+j//2])
		
		return markersWom_forR, markersMen_forR






