#!/usr/bin/env python3

## create a dictionary

switch = {'hostname':'sw1', 'ip':'10.0.1.1', 'version':'1.2', 'vendor':'cisco'}

## display parts of the dicitonary
print(switch['hostname'])
print(switch['ip'])
## request a 'fake' key
#print(switch['lynx'])

## request a fake key with get()
print("first test - .get()")
print(switch.get('lynx'))

print("second test - .get()")
print(switch.get('lynx', "the key is in another castle!"))

print("thirds test - .get()")
print(switch.get('version'))

print("fourth test- .keys()")
print(switch.keys())

print("Fith test- .values()")
print(switch.values())

print("sixth test - .pop()")
switch.pop("version") #removes this key and value pair
print(switch.keys())
print(switch.values()) 

print("seventh test - add a new value")
switch['adminlogin'] = 'kar108'
print(switch.keys())
print(switch.values())

print("eighth test - Add a new value")
switch['password'] = 'qwery'
print(switch.keys())
print(switch.values())


