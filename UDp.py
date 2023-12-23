import socket
import time

# Server address and port
server_address = ('localhost', 12000)

# Number of pings to send
num_pings = 10

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set timeout for the socket
client_socket.settimeout(1)

# Variables for RTT calculation
rtt_times = []

# Send pings
for sequence_number in range(1, num_pings + 1):
    # Prepare the ping message
    ping_message = f'Ping {sequence_number} {time.time()}'

    try:
        # Send the ping message to the server
        client_socket.sendto(ping_message.encode(), server_address)

        # Record the time when the ping was sent
        send_time = time.time()

        # Receive the response from the server
        response, server_address = client_socket.recvfrom(1024)

        # Record the time when the response is received
        receive_time = time.time()

        # Calculate round-trip time (RTT) in seconds
        rtt = receive_time - send_time

        # Append RTT to the list for later analysis
        rtt_times.append(rtt)

        # Print the response and RTT
        print(f'Response from {server_address}: {response.decode()} | RTT: {rtt:.6f} seconds')

    except socket.timeout:
        # Handle timeout (packet loss)
        print(f'Request timed out for Ping {sequence_number}')

# Close the socket
client_socket.close()

# Calculate and print statistics
if rtt_times:
    min_rtt = min(rtt_times)
    max_rtt = max(rtt_times)
    avg_rtt = sum(rtt_times) / len(rtt_times)
    packet_loss_rate = (num_pings - len(rtt_times)) / num_pings * 100

    print(f'\nPing statistics:')
    print(f'Min RTT: {min_rtt:.6f} seconds')
    print(f'Max RTT: {max_rtt:.6f} seconds')
    print(f'Avg RTT: {avg_rtt:.6f} seconds')
    print(f'Packet Loss Rate: {packet_loss_rate:.2f}%')
