from JSONify import JSON

db = JSON(
	'data.json', 
	indent=4, 
#	autosave=True
)


all = db.query.query_all()
print(all)

one = db.query.filter_by('f')
one['Water'] = 'lol'
db.edit('f', 'lol')
print(one)