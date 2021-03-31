import os
import pandas as pd


class SetOfParliamentMembers:
	def __init__(self, name):
		self.name = name
		
	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, sep=";") # pd.read_csv attend des valeurs séparées par une virgule. Nous sommes donc obligés de spécifier sep=";".
		
	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe
		
		
	def display_chart(self): # Run a chart of Men / Weman
		#see you later
		pass
	
	def split_by_political_party(self):
		result = {}
		data = self.dataframe
		
		all_parties = data["parti_ratt_finanacier"].dropna().unique()
		for party in all_parties:
			pass