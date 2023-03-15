# syntax for storing and exchanging data
# to use JSON in python you need to import the JSON module
import json
# converting from JSON to python
# json.loads() : result of this conversion is a python dictionary
x = '{"name":"joseph", "age":26 , "city":"Nairobi"}'
# parse x :
y = json.loads(x)
print(y)
print(type(y))
print(type(x))

# converting python to json
# json.dumps()
x = {"name":"joseph", "age":26 , "city":"Nairobi"}
# parse x
y = json.dumps(x)

print(y)
print(type(y))

# converting python objects into JSON strings
print(json.dumps(['apple','bananas']))
print(json.dumps(('apple','bananas')))
print(json.dumps(42))
print(json.dumps(42.0))
print(json.dumps(True))

# sort the keys of a JSON response
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))














