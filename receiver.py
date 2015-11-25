#this is receiver
import MyPacket
import MySocket
import config

print config.hostnameR

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameR, config.rPort))
socket.sock.listen(5)
print "listening on port %s" % config.rPort

while True:
	conn, c_adddr = socket.sock.accept()
	print c_adddr, conn
	revBuffer = conn.recv(1024)
	print revBuffer
	if not data:
		break

	seqNum = 1
	ackNum = 0
	ack = MyPacket.mypacket(1, 1, None, config.windowSize, ackNum)
	print "%s %s %s %s %s" % ack