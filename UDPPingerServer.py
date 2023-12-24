import random
from socket import *
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Started UDP server on port 12000")

previous_timestamp = None

try:
    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)

        sequence_number, current_timestamp = message.decode().split()[1], float(message.decode().split()[2])

        message = message.upper()

        if rand < 4:
            continue

        serverSocket.sendto(message, address)

        if previous_timestamp is not None:
            time_difference = current_timestamp - previous_timestamp
            print(f"Response from {address}: HEARTBEAT Number {sequence_number}, Time Difference: {time_difference} seconds")

        previous_timestamp = current_timestamp

except KeyboardInterrupt:
    print("\nClient Stopped. Server shutting down.")

finally:
    serverSocket.close()
