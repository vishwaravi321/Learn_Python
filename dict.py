obj = {'name': 'Vishwa', 
        'age': '21',
        'Country' : "India"}
print(obj)
print(type(obj))
print(obj.keys())
print(obj.values())

print(obj.items())  #show keys and values in tuple format...

print(obj['Country'])
print(obj.get('name'))

obj.update({'Country' : 'japan'})
print(obj)

obj.update({'height' : 6})
print(obj)

obj['height'] = 5
print(obj)
