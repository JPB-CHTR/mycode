#!/usr/bin/env python3

import pyexcel

def get_ip_data(head1,head2):
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What isthe driver associated with this device? ")
    d = {head1 : input_ip, head2 : input_driver}
    return d

mylistdict = []

print("Hello! This program will make you a *.xls file")
col_head1 = input("What would you like to name column 1? ")
col_head2 = input("What would you like to name column 2? ")

while(True):
    mylistdict.append(get_ip_data(col_head1,col_head2)) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
