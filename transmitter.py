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

def sendEot(connection, seqNum):
	print "Sending FIN"
	eot = MyPacket.mypacket(3, seqNum, None, config.windowSize, None)
	eot = pickle.dumps(eot)
	connection.sendall(eot)

with open(argument[1], 'r') as f:
	seqNum = 1
	resend = False
	eotSent = False
	cachePacket = []
	while True:
		# loops through the window
		if eotSent == False:
			for i in xrange(config.windowSize):
				if resend:
					# temp = pickle.loads(cachePacket[i])
					# print "resending packets: %s" % (temp.seqNum)
					time.sleep(0.01)
					socketT.sock.sendall(cachePacket[i])
				else:
					
					read_data = f.read(1)
					# pack data in packet
					print 'sending packet. Sequence Number: %s. Type: %s' % (seqNum, 'Data')
					packet = MyPacket.mypacket(2, seqNum, read_data, config.windowSize, None)
					seqNum += 1
					# encode packet
					packet = pickle.dumps(packet)
					# put packets in the cache array
					cachePacket.append(packet)
					# send encoded packet
					socketT.sock.sendall(packet)
				
		# reset variable after for loop
		resend = False

		try:
			# set socket timeout for receiving ack
			socketT.sock.settimeout(0.01)
			# wait and receive ack
			ack = socketT.sock.recv(config.BUFFER_SIZE)
		except socket.error, e:
			err = e.args[0]
			# if timed out, that means ack is not received
			if(err == 'timed out'):
				resend = True
				print "No ACK received, sending previous window again"
				pass

		else:
			if ack:
				# decode ack
				recvAck = pickle.loads(ack)
				print "ack received, ACK Number: %s" % (recvAck.ackNum)
				# if ACK is EOT, it is a FIN ACK
				if recvAck.type == 3:
					print "FIN ACK received, closing connection"
					socketT.sock.close()
					break

		if resend == False:
			# reset cache packet array if resend is false
			cachePacket = []

		if not read_data and resend == False:
			print "------ end of the file -------"
			eotSent = True
			sendEot(socketT.sock, seqNum)

f.closed





