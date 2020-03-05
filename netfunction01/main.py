#!/usr/bin/env python3

def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connection with ' + coffeetime )
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
        print()

def devicereboot(ips_list):
    for x in ips_list.keys():
        print(f"Connecting to..{x}")
        print("REBOOTING NOW!")

def main():
    file = open("ip_input.csv", "r")
    work2do = csv.reader(file)

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(work2do)
    devicereboot(work2do)

main()
