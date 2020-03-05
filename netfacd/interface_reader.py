#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

choice=input("Please choose one of the above interfaces: ")

print('\n***********Details of Interface - ' + choice + ' **********')
try:
    print('MAC: ', end='')
    print((netifaces.ifaddresses(choice)[netifaces.AF_LINK])[0]['addr'])
    print('IP: ', end='')
    print((netifaces.ifaddresses(choice)[netifaces.AF_INET])[0]['addr'])
except:
    print('Could not collect adapter information')
