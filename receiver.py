#this is receiver
import MyPacket
import MySocket
import config
import pickle

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameR, config.portB))
socket.sock.listen(5)
print "listening on port %s" % config.portB

# initialize sequence number
seqNum = 1
count = 0

while True:
	print "Waiting for connections"
	conn, c_adddr = socket.sock.accept()
	print c_adddr, conn

	while True:
		recvBuffer = conn.recv(1024)
		if not recvBuffer:
			break

		# if there are data
		if recvBuffer:
			# decode data
			recvPacket = pickle.loads(recvBuffer)
			# assign variables
			data = recvPacket.data
			seqNum = recvPacket.seqNum
			ackNum = seqNum + 1
			count += 1
			print "packet %s received" % (seqNum)
			# encode ack
			if seqNum % 8 == 0:
				if count == 8: 
					ack = pickle.dumps(MyPacket.mypacket(1, 1, None, config.windowSize, ackNum))
					print "send ACK: %s" % (ackNum)
					conn.send(ack)

				# reset count
				count = 0


	# ack = MyPacket.mypacket(1, 1, None, config.windowSize, ackNum)
	# 		conn.send()
