# Python Libraries
from socket import*     # Sockets
from subprocess import* # Linux commands 
import os               # for changing directory

server_port = 10100

# Create TCP welcoming socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))

# Server begins listening for incoming requests
server_socket.listen(1)
print('The server is ready to receive')

# Loop forever: standby for clients to connect
while True:
	# Server waits on accept() for incoming requests
	# New socket created on return
	client_connection, addr = server_socket.accept()

	# loop forever: stanby for client requests
	while True:
		# receive command
		cmd = client_connection.recv(1024).decode()

		# split contents to refer to base command
		cmd_split = cmd.split()

		# client requested to close connection
		if(cmd_split[0] == 'exit'):
			client_connection.close()
			break
		# change directory
		elif(cmd_split[0] == 'cd'):
			current_dir = os.getcwd() # Get server's current directory path name
			print(current_dir) # print current directory of server before cd
			change_dir = current_dir + '/' + cmd_split[1] # form the path name to change to
			os.chdir(change_dir) # system call to change directory to desired directory by client
			msg = '\n'
			client_connection.sendall(msg.encode())
			current_dir = os.getcwd() # Get server's current directory path name
			print(current_dir) # print current directory of server after cd
		# HTTP Requests
		elif(cmd_split[0] == 'HEAD' or cmd_split[0] == 'GET'):
			output = "doesn't work"
			print(output)
			client_connection.sendall(output_encode())
		# run linux commands on server side, send output to client
		else:
			# run command using subprocess library
			input = Popen(cmd, shell=True, stdout=PIPE, universal_newlines=True)
			# Get server output: reads the captured output from running command
			# captured output is in stdout and typecasted into a string
			output=str(input.stdout.read())

			# program hanged if output was an empty string
			if(output == ""):
				output = "\n"
				
			# Send server response to client
			# translate string output into byte code, send to client
			print(output)
			client_connection.sendall(output.encode())