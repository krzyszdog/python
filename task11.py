import os

os.system("ping 8.8.8.8 > ping.txt")

with open("ping.txt", "r") as file:
    for line in file:
        nl = line.replace("\n", "")
        if "TTL" in nl:
            reply = nl.split(" ")
            byte = reply[3].split("=")
            byte1 = byte[1]
            ms = reply[4].split("=")
            ms1 = ms[1]
            print(f"Sent bytes: {byte1}\trelay time: {ms1}")
