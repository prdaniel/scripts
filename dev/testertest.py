import socket
hostip = socket.gethostbyname(socket.gethostname())
prodigit = int(hostip[-1]) + 1
prodip = hostip.replace(hostip[-1],str(prodigit))
print prodip
