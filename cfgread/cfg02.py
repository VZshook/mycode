#!/usr/bin/env python3
## create file object in "r"ead mode
name=input("name of file to load? ")
configfile = open(name, "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)
row_count= sum( 1 for row in "vlanconfig.cfg")
print(row_count)

## Always close your file
configfile.close()
