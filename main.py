from JSONify import JSON

db = JSON(
	'data.json', 
	indent=4, 
#	autosave=True
)

db.add('Water', 'Lava')
all = db.query.query_all()
print(all)