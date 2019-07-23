#!/usr/bin/env python3
ipchk = input("apply an ip address: ") 

if ipchk== "192.168.70.1":
        print("Looks like the ip was set:"+ ipchk + "this is not recomended")
elif ipchk:
        print("looks like the IP address was set: "+ ipchk)
else: 
        print("you did not provide input")
