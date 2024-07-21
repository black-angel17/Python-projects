import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)
print('Connected to {}:{}'.format(*server_address))

try:
    # Send data to the server
    message = 'Hello, server!'
    client_socket.sendall(message.encode())
    print('Sent message: {}'.format(message))

    # Receive a response from the server
    response = client_socket.recv(1024).decode()
    print('Received response: {}'.format(response))

finally:
    # Close the connection
    client_socket.close()
    print('Connection closed')
