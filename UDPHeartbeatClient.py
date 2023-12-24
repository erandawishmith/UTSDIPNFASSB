import time
from socket import *

serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

num_heartbeats = 10
heartbeat_times = []

for i in range(1, num_heartbeats + 1):
    heartbeat_message = f"Heartbeat {i} {time.time()}"
    clientSocket.sendto(heartbeat_message.encode(), (serverName, serverPort))

    try:
        response, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - float(response.decode().split()[2])
        heartbeat_times.append(rtt)
        print(f"Response from {serverAddress}: {response.decode()}, RTT: {rtt:.6f} seconds")

    except timeout:
        print(f"Heartbeat {i} timed out")

if heartbeat_times:
    print(f"\nMinimum Heartbeat RTT: {min(heartbeat_times):.6f} seconds")
    print(f"Maximum Heartbeat RTT: {max(heartbeat_times):.6f} seconds")
    print(f"Average Heartbeat RTT: {sum(heartbeat_times) / len(heartbeat_times):.6f} seconds")
    print(f"Heartbeat Packet Loss Rate: {(num_heartbeats - len(heartbeat_times)) / num_heartbeats * 100:.2f}%")

clientSocket.close()
