import subprocess
import socket
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

# Open a shell and run a command
def shell(x):
    shell_command = x
    output = run_command(shell_command)
    return output



# Telnet server details
HOST = '192.168.170.1'
PORT = 1235  # Default Telnet port

# Function to process Telnet data
def process_telnet_data(data):
    # Process and interpret the Telnet data here
    # For demonstration purposes, we will simply print the received data
    d=shell(data)

    # Send a response back to the client
    response = "Response from server: {}".format(d.upper())
    print(response)
    client_socket.send(d.encode('utf-8'))

# Create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(3)
print("Telnet server is listening on {}:{}".format(HOST, PORT))

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print("Accepted connection from:", client_address)
print("Accepted connection from:", client_socket)
allocated_port = client_socket.getsockname()[1]
print("Allocated port for client socket:", allocated_port)



# Receive and process Telnet data
while True:
    # Wait for Telnet data
    raw_data = client_socket.recv(1024).decode('utf-8')

    # If no data is received, exit the loop
    if not raw_data:
        break

    # Split the received data into individual lines
    lines = raw_data.split('\n')

    # Process each line of Telnet data
    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Process the Telnet data
        process_telnet_data(line)

# Close the client socket and server socket
client_socket.close()
server_socket.close()
