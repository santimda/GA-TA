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

		# Read THE sheet and Create a sheetData atribute with the info of the file
		self.sheetData = allFile.parse(self.sheet0)
		
		# create column name and column values 
		self.fileColumn, self.fileValues = self.sortData()
		self.n_women, self.n_men, self.total_MenWomen = self.WoMens() 	
		self.n_each_population, self.totalPopulations = self.Populations()
		self.n_markers = self.Markers()

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
		countWomen_i=0
		countMen_i=0
		
		#inicializo la primer subpoblacion
		sex_index, pop_index = self.fileValues.T[1], self.fileValues.T[2]
		index = pop_index[0]
		#para cada subpoblacion, cuento
		for i,each in enumerate(pop_index):
		    
		    if pop_index[i] == index and sex_index[i] == 2:
		        countWomen_i += 1
		    elif pop_index[i] == index and sex_index[i] == 1:
		        countMen_i += 1
		    if i < len(pop_index)-1 and pop_index[i+1] == index + 1:
		        index += 1    
		        countWomen.append(countWomen_i/2)
		        countMen.append(countMen_i)
		        countWomen_i=0
		        countMen_i = 0
		    elif i == len(pop_index)-1:
		        countWomen.append(countWomen_i/2)
		        countMen.append(countMen_i)
		total_subpop = np.array(countWomen)+np.array(countMen)
		number_subpop = len(total_subpop)
		
		return total_subpop, number_subpop

	def Markers(self):
		#return number of markers
		return len(self.fileValues.T[3:])

