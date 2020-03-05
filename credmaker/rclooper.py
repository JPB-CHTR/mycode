#!/usr/bin/env python3

import csv

def autoread():
    f = open("csv_users.txt", "r")
    i=0
    for row in csv.reader(f):
        i = i + 1
        filename = "admin.rc%d"%(i)
        rcfile = open(filename, "w")
        print("export OS_AUTH_URL=" + row[0], file=rcfile)
        print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
        print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
        print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
        print("export OS_USERNAME=" + row[3], file=rcfile)
        print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
        rcfile.close()

def manual(x):
    outFile = open("adminrc" + x, "a")
    osAUTH = input("What is the OS_AUTH+URL?")
    print("export OS_AUTH_URL=" + osAUTH, file = outFile)
    print("export OS_IDENTITY_API_VERSION=3", file = outFile)
    osPROJ = input("What is the OS_PROJECT_NAME?")
    print("export OS_PROJECT_NAME=" + osPROJ, file = outFile)
    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)
    osUSER = input("What is the OS_USERNAME?")
    print("export OS_USERNAME=" + osUSER, file=outFile)
    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)
    osPASS = input("What is the OS_PASSWORD?")
    print("export OS_PASSWORD=" + osPASS, file=outFile)
    outFile.close()

choice=input("Please choose 1 to import csv automatically or 2 to manually create a adminrc file")
if choice == "1":
    autoread()
elif choice == "2":
    des=input("Please enter file designator")
    manual(des)
else:
    print(f"Man seriously? {choice}, I said 1 or 2")

