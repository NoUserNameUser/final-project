import socket
import sys
import MyPacket
import MySocket
import config

# IP Address for Transmitter
host = config.hostnameT

# Creates a TCP/IP socket
socket = MySocket.mysocket()

socket.sock.connect((config.hostnameNE, config.rPort))

argument = sys.argv
print argument

with open(argument[1], 'r') as f:
	seqNum = 0
	while True:
		for i in xrange(8):
			read_data = f.read(1)
			packet = MyPacket.mypacket(2, seqNum, read_data, config.windowSize, None)
			seqNum += 1
			print read_data
			socket.sock.sendall(read_data)
		print '====================', seqNum
		if not read_data:
			break
f.closed





