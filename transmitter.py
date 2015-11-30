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
	seqNum = 1
	resend = False
	cachePacket = []
	while True:
		for i in xrange(config.windowSize):
			if resend:
				# temp = pickle.loads(cachePacket[i])
				# print "resending packets: %s" % (temp.seqNum)
				time.sleep(0.001)
				socketT.sock.sendall(cachePacket[i])
			else:
				
				print 'sending packet. Sequence Number: %s' % (seqNum)
				read_data = f.read(1)
				packet = MyPacket.mypacket(2, seqNum, read_data, config.windowSize, None)
				seqNum += 1
				# encode packet
				packet = pickle.dumps(packet)
				# put packets in the cache array
				cachePacket.append(packet)
				# send encoded packet
				socketT.sock.sendall(packet)
				
		# reset resend variable after for loop
		resend = False
		print '====================', seqNum

		try:
			socketT.sock.settimeout(0.1)
			ack = socketT.sock.recv(1024)
		except socket.error, e:
			err = e.args[0]
			# if timed out, that means ack is not received
			if(err == 'timed out'):
				resend = True
				print "No ACK received, sending same window again"
				pass

		else:
			if ack:
				# decode ack
				recvAck = pickle.loads(ack)
				print "ack received, ACK Number: %s" % (recvAck.ackNum)

		if resend == False:
			# reset cache packet array if resend is false
			cachePacket = []

		if not read_data:
			break
f.closed





