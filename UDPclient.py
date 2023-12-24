import time
from socket import *

serverName = ""
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

num_pings = 10

rtt_times = []

for i in range(1, num_pings + 1):
    message = f"Ping {i} {time.time()}"

    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        response, serverAddress = clientSocket.recvfrom(1024)

        rtt = time.time() - float(response.decode().split()[2])
        rtt_times.append(rtt)

        print(f"Response from {serverAddress}: {response.decode()}, RTT: {rtt:.6f} seconds")

    except timeout:
        print(f"Request timed out")

if rtt_times:
    print(f"\nMinimum RTT: {min(rtt_times):.6f} seconds")
    print(f"Maximum RTT: {max(rtt_times):.6f} seconds")
    print(f"Average RTT: {sum(rtt_times) / len(rtt_times):.6f} seconds")
    print(f"Packet Loss Rate: {(num_pings - len(rtt_times)) / num_pings * 100:.2f}%")

clientSocket.close()
