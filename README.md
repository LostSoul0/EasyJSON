# Installation
```
pip install JSONify
```
# Usage

JSONify is a package i made for people to ease the use of JSON files
```py
from JSONify import JSON
json = JSON("JSON_FILE_LOCATION", indent=4)
```

You can now use it like any other db, but its a json!

#### Adding data
```py
db.add('Water', 'Lava')
db.query.all()
#{"Water": "Lava"}
```

#### Editing data
```py
db.edit('Water', 'Air')
db.query.all()
#{"Water": "Air"}
```

#### Removing data
```py
db.delete('Water')
db.query.all()
#{}
```

#### Clear JSON
```py
db.reset()
#{}
```

#### Getting all the data
```py
db.add('Water', 'Lava')
db.add('Air', 'Soil')
db.query.all()
#{"Water": "Lava", "Air": "Soil"}
```

#### Getting specific data
```py
db.query.filter_by('Water')
#'Lava'
db.query.filter_by('Lava')
#None
```