import socket
import sys
import MyPacket
import MySocket
import config
import pickle
import time

# Creates a TCP/IP socketT
socketT = MySocket.mysocket()

socketT.sock.connect((config.hostnameNE, config.portA))

argument = sys.argv
print argument

with open(argument[1], 'r') as f:
	seqNum = 0
	noAck = False
	cachePacket = []
	while True:
		for i in xrange(8):
			print noAck
			if noAck:
				print 'in'
				socketT.sock.sendall(cachePacket[i])
			else:
				print 'in else'
				read_data = f.read(1)
				packet = MyPacket.mypacket(2, seqNum, read_data, config.windowSize, None)
				seqNum += 1
				# print read_data
				packet = pickle.dumps(packet)
				cachePacket.append(packet)
				# print packet
				socketT.sock.sendall(packet)
				
		# reset noAck variable after for loop
		noAck = False
		print '====================', seqNum

		try:
			socketT.sock.settimeout(1)
			ack = socketT.sock.recv(1024)
		except socket.error, e:
			err = e.args[0]
			# if timed out, that means ack is not received
			if(err == 'timed out'):
				noAck = True
				print "No ACK received, sending same window again"
				pass

		# time.sleep(1)
		

		if not read_data:
			break
f.closed





