import socket
# comment
# Creates a TCP/IP socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connects as client 
socket.connect((hostname, portnumber))

