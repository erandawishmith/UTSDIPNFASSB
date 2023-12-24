import time
from socket import *

# Server details
serverName = ''  # Replace with the actual server IP address
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout for the socket (1 second)
clientSocket.settimeout(1)

# Number of pings to send
num_pings = 10

# Track round-trip times
rtt_times = []

for i in range(1, num_pings + 1):
    # Build the ping message
    message = f"Ping {i} {time.time()}"

    # Send the ping message to the server
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        # Receive the response from the server
        response, serverAddress = clientSocket.recvfrom(1024)
        
        # Calculate round-trip time
        rtt = time.time() - float(response.decode().split()[2])
        rtt_times.append(rtt)

        # Print the response message and round-trip time
        print(f"Response from {serverAddress}: {response.decode()}, RTT: {rtt:.6f} seconds")

    except timeout:
        # Handle timeout (packet loss)
        print(f"Request timed out")

# Calculate and print statistics
if rtt_times:
    print(f"\nMinimum RTT: {min(rtt_times):.6f} seconds")
    print(f"Maximum RTT: {max(rtt_times):.6f} seconds")
    print(f"Average RTT: {sum(rtt_times) / len(rtt_times):.6f} seconds")
    print(f"Packet Loss Rate: {(num_pings - len(rtt_times)) / num_pings * 100:.2f}%")

# Close the socket
clientSocket.close()
