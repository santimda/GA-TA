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
		
	def read(self):
#		self.__init__(inputTable)
		return self.fileColumn, self.fileValues

	def sortData(self):
		columnName=[]
		for each in self.sheetData.columns:
			columnName.append(each)
		columnValues = []
		for each in self.sheetData.values:
			columnValues.append(each)

		return columnName, columnValues
