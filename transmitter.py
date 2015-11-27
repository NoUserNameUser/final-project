import socket
import sys
import MyPacket
import MySocket
import config
import pickle
import time

# Creates a TCP/IP socket
socket = MySocket.mysocket()

socket.sock.connect((config.hostnameNE, config.portA))

argument = sys.argv
print argument

with open(argument[1], 'r') as f:
	seqNum = 0
	while True:
		for i in xrange(8):
			read_data = f.read(1)
			packet = MyPacket.mypacket(2, seqNum, read_data, config.windowSize, None)
			seqNum += 1
			# print read_data
			packet = pickle.dumps(packet)
			print packet
			socket.sock.sendall(packet)

			recvAck = socket.sock.recv(config.BUFFER_SIZE)
 
		print '====================', seqNum
		time.sleep(1)
		if not read_data:
			break
f.closed





