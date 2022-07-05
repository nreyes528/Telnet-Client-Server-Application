# Python Libraries
from socket import*
import sys

# Connect to server based on command line arguments (ip, port)
server_name = (sys.argv[1])
server_port = int((sys.argv[2]))

# Create TCP socket for server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

# infinite loop: continually send commands to server
while True:

	# user input for command line
	cmd = input('Enter a command: ')

	# split contents to refer to base command
	cmd_split = cmd.split()

	# Send server command
	client_socket.send(cmd.encode())

	# Exit connection with server
	if(cmd_split[0] == 'exit'):
		break
	# HTTP HEAD and GET requests
	elif(cmd_split[0] == 'HEAD' or cmd_split[0] == 'GET'):
		# receive response from server
		msg = client_socket.recv(1024).decode()

		# print server response
		print(msg)
	# Linux Command requests to Server
	else:
		# receive response from server
		msg = client_socket.recv(1024).decode()

		# print server response
		print(msg)

# close client
client_socket.close()