#!/usr/bin/env python3
hostname = input("what value should we set for hostname?")

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

else:
    print(f"Why would you type {hostname}, you idiot!")

#Always show that the program is ending
print("Exiting the script")
