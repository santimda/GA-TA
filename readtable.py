import numpy as np
import pandas as pd

class Data():
	
	'''a person is any one in the file'''
	
	def __init__(self, inputTable):
		'''use Pandas'''
		file = inputTable

		# Load file
		
		allFile = pd.ExcelFile(file)

		# nos quedamos con la primer hoja, que pasa si hay mas? 
		sheet0 = allFile.sheet_names
		
		sheet0_data = allFile.parse(sheet0)

		self.sheet0_data = sheet0_data

	def read(self):
#		self.__init__(inputTable)

		return self.sheet0_data


