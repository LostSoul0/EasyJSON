import json
class Query:
	def __init__(self, db):
		self.db = db

	""" Query the JSON with a key """
	def query_all(self, mode='DICTIONARY'):
		mode = mode.upper()
		with open(self.db,'r') as f:
			data = json.load(f)	
		
		if mode == 'DICTIONARY':
			return data


	""" Query the JSON with a key """
	def filter_by(self, key, mode='DICTIONARY'):
		mode = mode.upper()
		with open(self.db,'r') as f:
			data = json.load(f)	
		
		if mode == 'DICTIONARY':
			try:
				return data[key]
			except ValueError:
				return None