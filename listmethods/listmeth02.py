#!/usr/bin/env python3
proto = ["ssh, http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
protoa.append("dns")
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
protoa.insert(0,"this is akward") #adding a item to the beginning of a list
print(protoa)
port = int(input("What port do you want to add to the list?"))
proto2.append(port)
print(proto2)
