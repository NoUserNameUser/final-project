#this is receiver
import MyPacket
import MySocket
import config

print config.hostnameR

# socket = MySocket.mysocket()
# socket.sock.bind((config.hostnameR, 9000))
# socket.sock.listen(5)

# a packet contains type, sequence number, data, window size, ack number
packet = MyPacket.mypacket('01', 1, 1, 8, None)

print packet.type