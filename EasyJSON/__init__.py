import os
import json
from .query import Query

class JSON:
	def __init__(self, json_file=None, indent=None):
		if json_file:
			self.db = json_file
		else:
			self.temp = open("mydatabase.json", "w+")
			self.temp.write("{}")
			self.temp.close()
			self.db = "mydatabase.json"

		self.query = Query(self.db)
		self.indent = indent
	

	""" Add a key to the JSON """
	def add(self, key, value):
		with open(self.db,'r') as f:
			data = json.load(f)
		data[key] = value
		with open(self.db,'w') as f:
			json.dump(data, f, indent=self.indent)


	""" Delete a key off the JSON """
	def delete(self, key):
		try:
			with open(self.db,'r') as f:
				data = json.load(f)
			del data[key]
			with open(self.db,'w') as f:
				json.dump(data, f, indent=self.indent)
		except KeyError:
			print(f"Could not find {key} in database!")


	""" Edit a key of the JSON """
	def edit(self, key, value):
		with open(self.db,'r') as f:
			data = json.load(f)

		for val in data:
			if val == key:
				data[key] = value


		with open(self.db,'w') as f:
			json.dump(data, f, indent=self.indent)

	""" Clear all of the JSON """
	def reset(self):
		with open(self.db,'w') as f:
			f.truncate(0)
			f.write("{}")