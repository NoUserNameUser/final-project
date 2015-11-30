#this is receiver
import MyPacket
import MySocket
import config
import pickle


# loop to find if the sequence number is in the buffer already
def seqNumInArray(array, element):
	for i in xrange(config.windowSize):
		if isinstance(array[i], list):
			if array[i][0] == element:
				return True
	return False

def windowFull(array):
	for i in xrange(config.windowSize):
		if array[i] == None:
			return False
	return True

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameNE, config.portB))
socket.sock.listen(5)
print "listening on port %s" % config.portB

# initialize sequence number
seqNum = 1
buffWin = [None] * config.windowSize

while True:
	print "Waiting for new connections"
	conn, c_adddr = socket.sock.accept()
	print c_adddr, conn

	while True:
		recvBuffer = conn.recv(config.BUFFER_SIZE)
		if not recvBuffer:
			break

		# if there are data
		if recvBuffer:
			# decode data
			recvPacket = pickle.loads(recvBuffer)
			print "Packet type: ", recvPacket.type
			# if eot received
			if recvPacket.type == 3:
				print "FIN received"
				# send FIN ACK to transmitter
				finAck = pickle.dumps(MyPacket.mypacket(3, 1, None, config.windowSize, ackNum+1))
				print "sending FIN ACK"
				conn.sendall(finAck)

				print "connection closed"
				# close connection
				conn.close()
				break
			# assign variables
			data = recvPacket.data
			seqNum = recvPacket.seqNum
			ackNum = seqNum + 1
			print "packet %s received" % (seqNum)

			# this packet is not in the buffer window
			if seqNumInArray(buffWin, seqNum) == False:
				# put the packet in the buffer window
				for i in xrange(config.windowSize):
					if buffWin[i] == None:
						buffWin[i] = [seqNum, data]
						break

			print buffWin
			# encode ack
			if seqNum % config.windowSize == 0:
				if windowFull(buffWin): 
					ack = pickle.dumps(MyPacket.mypacket(1, 1, None, config.windowSize, ackNum))
					print "send ACK: %s" % (ackNum)
					conn.sendall(ack)
					# reset buffWindow
					buffWin = [None] * config.windowSize


	# ack = MyPacket.mypacket(1, 1, None, config.windowSize, ackNum)
	# 		conn.send()

