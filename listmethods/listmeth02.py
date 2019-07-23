#!/usr/bin.env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns')  # will add dns to end of the list
protoa.append('dns') # Will add dns to end of list
print(proto)
proto2= [22, 80, 443, 53] # list 
proto.extend(proto2) # entends by the list proto2
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


