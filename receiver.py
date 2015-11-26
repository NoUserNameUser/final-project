#this is receiver
import MyPacket
import MySocket
import config
import pickle

print config.hostnameR

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameR, config.rPort))
socket.sock.listen(5)
print "listening on port %s" % config.rPort

# initialize sequence number
seqNum = 0

while True:
	conn, c_adddr = socket.sock.accept()
	print c_adddr, conn
	while True:
		revBuffer = conn.recv(1024)
		if not revBuffer:
			break

		if revBuffer:
			recvPacket = pickle.loads(revBuffer)
			data = recvPacket.data
			seqNum = recvPacket.seqNum

	# increament sequence number
	seqNum += 1
	ackNum = 0
	# ack = MyPacket.mypacket(1, 1, None, config.windowSize, ackNum)
	# print "%s" % ack.data