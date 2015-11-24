#this is receiver
import MyPacket
import MySocket
import config

print config.hostnameR

socket = MySocket.mysocket()
socket.sock.bind((config.hostnameR, config.rPort))
socket.sock.listen(5)
print "listening on port %s", rPort

# a packet contains type, sequence number, data, window size, ack number
packet = MyPacket.mypacket('01', 1, 1, 8, None)

print packet.type