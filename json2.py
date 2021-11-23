# Python object ko json data main convert karne ka program likho         
import json
m= {
    "name": "David",
    "class":"I",
    "age": 6
}

c=json.dumps(m)
print(c)