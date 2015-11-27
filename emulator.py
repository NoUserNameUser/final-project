import socket
import sys
import MyPacket
import MySocket
import config
import time
import random

socketT = MySocket.mysocket()
socketT.sock.bind(('', config.portA))
socketT.sock.listen(5)
print "listening on port %s" % config.portA


socketR = MySocket.mysocket()
socketR.sock.connect((config.hostnameR, config.portB))

while True:
	conn, c_adddr = socketT.sock.accept()
	print c_adddr, conn
	while True:
		recvBuffer = conn.recv(config.BUFFER_SIZE)

		if random.random() > config.dropRate:
			print ('Dropped packet from {}' .format(c_adddr))
			continue

		if not recvBuffer:
			break

		if recvBuffer:
			socketR.sock.sendall(recvBuffer)
			fromRecv = socketR.sock.recv(config.BUFFER_SIZE)
			if fromRecv:
				socketT.sock.sendall(fromRecv)