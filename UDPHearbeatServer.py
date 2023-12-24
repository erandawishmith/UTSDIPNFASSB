import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Started UDP server on port 12000")

try:
    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)

        sequence_number, timestamp = message.decode().split()[1], float(message.decode().split()[2])

        message = message.upper()

        if rand < 4:
            continue

        serverSocket.sendto(message, address)

        print(f"Heartbeat from {address}: Sequence Number {sequence_number}, Timestamp {timestamp}")

except KeyboardInterrupt:
    print("\nClient Stopped. Server shutting down.")

finally:
    serverSocket.close()
