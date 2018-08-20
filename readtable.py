import numpy as np
import pandas as pd

'''(Martin 09/07). 	Pandas no soporta archivos openOffice, deberiamos adaptar la lectura para este tipo de archivos. 
					Pandas solo lee las columnas que tienen un header (cabecera). Por ejemplo en el archivo planilla_generica.xlsx
					no reconoce al lugar (Posadas, Corrientes,etc) como columna con informacion'''
					
class Data():
	
	'''a person is any one in the file'''
	
	def __init__(self, inputTable):
		'''use Pandas'''
		file = inputTable

		# Load file
		
		allFile = pd.ExcelFile(file)

		# Only one sheet admited  
		if len(allFile.sheet_names) > 1: 
			raise ValueError('The program does not support more than 1 sheet')
		elif len(allFile.sheet_names) == 1: 
			self.sheet0 = allFile.sheet_names[0]

		# Read THE sheet and Create a sheetData atribute with all the info of the file
		self.sheetData = allFile.parse(self.sheet0)
		
		# create column name and column values 
		self.nameColumn, self.fileValues = self.sortData()
		self.n_women, self.n_men, self.total_MenWomen = self.WoMens() 	
		self.men4subpop, self.women4subpop, self.n_each_population, self.totalPopulations,self.populations = self.Populations()
		self.n_markers, self.markers = self.Markers()
		
	def sortData(self):
		columnName=[]
		for each in self.sheetData.columns:
			columnName.append(each)
		columnValues = []
		for each in self.sheetData.values:
			columnValues.append(each)

		return np.array(columnName), np.array(columnValues)

	def WoMens(self):
		'''return number of women, mens and total in the file'''
		countWomen = 0
		countMen = 0

		for each in self.fileValues.T[1]:
			#print each
			if each == 2:
				countWomen += 1
			elif each == 1:
				countMen += 1

		# countWomen = countWomen/2 for convention
		return countWomen/2, countMen, countWomen/2 + countMen 

	def Populations(self):
		'''return total number of populations of the study'''

		countWomen = []
		countMen = []
		#inicializo contador de hombres y mujeres en cada subpoblacion
		countWomen_i = 0
		countMen_i = 0
		
		#inicializo la primer subpoblacion
		#pop_index = array que toma etiquetas de poblaciones
		#sex_index = array con los valores del sexo

		sex_index, pop_index = self.fileValues.T[1], self.fileValues.T[2]
		index = pop_index[0]

		# will store women and mens for each population. shape(popul) = (#populations,...)
		popul = []

		# para cada subpoblacion, cuento
		aux=[]
		for i,each in enumerate(pop_index):
			
			# auxiliar for save mens and women for one population
			if each == index and sex_index[i] == 2:
				#count a women
				countWomen_i += 1
				aux.append(self.fileValues[i])
			elif each == index and sex_index[i] == 1:
				#count a men
				countMen_i += 1
				aux.append(self.fileValues[i])
			# partial save of women and men populations if i<len() then we continue saveing, if not, then save the last populations
			if i < len(pop_index)-1 and pop_index[i+1] == index + 1:
				index += 1    
				countWomen.append(countWomen_i/2)
				countMen.append(countMen_i)
				countWomen_i=0
				countMen_i = 0
				popul.append(aux)
				aux = []
			elif i == len(pop_index)-1:
				countWomen.append(countWomen_i/2)
				countMen.append(countMen_i)
				popul.append(aux)

		total_subpop = np.array(countWomen)+np.array(countMen)
		number_subpop = len(total_subpop)
		
		return countMen, countWomen, total_subpop, number_subpop, popul

	def Markers(self):
		#return number of markers
		#print self.fileValues[205]
		return len(self.fileValues.T[3:]), self.nameColumn.T[3:]




