import socket
import sys
import MyPacket

# Creates a TCP/IP socket
#socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connects as client 
#socket.connect((hostname, portnumber))

argument = sys.argv
print argument



with open(argument[1], 'r') as f:
	while True:
		seqNum = 0
	   for i in xrange(8):
	   	read_data = f.read(1)
	   	packet = MyPacket.mypacket(2, seqNum, read_data, 8, None)
	   	seqNum++
	   	print read_data
	   print '===================='
	   if not read_data:
	   	break
f.closed





