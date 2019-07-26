#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try: 
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

def listy(lis):
    for name in lis:
        print(netifaces.ifaddresses(name)[netifaces.AF_INET][0]['addr'])
        print(netifaces.ifaddresses(name)[netifaces.AF_LINK][0]['addr'])
#in_name = input("enter name: ")
listy(netifaces.interfaces())

