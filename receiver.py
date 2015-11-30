#this is receiver
import MyPacket
import MySocket
import config
import pickle

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameNE, config.portB))
socket.sock.listen(5)
print "listening on port %s" % config.portB

# initialize sequence number
seqNum = 0

while True:
	print "Waiting for connections"
	conn, c_adddr = socket.sock.accept()
	print c_adddr, conn

	while True:
		recvBuffer = conn.recv(1024)
		if not recvBuffer:
			break

		if recvBuffer:
			recvPacket = pickle.loads(recvBuffer)
			data = recvPacket.data
			seqNum = recvPacket.seqNum
			print "packet %s received sending ACK" % (seqNum)

	# ack = MyPacket.mypacket(1, 1, None, config.windowSize, ackNum)
	# 		conn.send()

	# increament sequence number
	seqNum += 1
	ackNum = 0
	# print "%s" % ack.data