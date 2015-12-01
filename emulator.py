############################################
# File name: Network Emulator (emulator.py)#                  
# Author: Jackie Ye & Reymon Mercado       #              
# Assignment: FINAL PROJECT for COMP 7005  #                 
# Instructor: Aman Abdulla                 #    
############################################

import socket
import sys
import MyPacket
import MySocket
import config
import random
import pickle

# Creates a TCP/IP socket called "socketT" for the transmitter (transmitter.py)
socketT = MySocket.mysocket() 

# Binds the TCP/IP socket to the port, "portA"
socketT.sock.bind(('', config.portA))

# Listens for incoming connections coming from the transmitter 
socketT.sock.listen(5)
print "Listening on port %s" % config.portA

count = 1

# Mainloop of the network emulator
while True:

	# Accepts connections from the specified socket for the transmitter, "socketT"
	conn, c_addr = socketT.sock.accept()
	print c_addr, conn

	# Creates a TCP/IP socket called "socketR" for the receiver (receiver.py)
	socketR = MySocket.mysocket()

	# Connects the TCP/IP socket, "socketR", to the port, "portB"
	socketR.sock.connect((config.hostnameR, config.portB))
	print "Connected to port %s" % config.portB
	
	while True:

		# Receives the data from the connection in small chunks, which value is 
		# established in it's buffer size defined in the config.py file (1024)
		recvBuffer = conn.recv(config.BUFFER_SIZE)

		# Randomly discards packets if the random number generated is greater than the
		# drop rate specified in the config.py file. Packets drop 20% of the time
		if random.random() < config.dropRate:
			print '---------- Dropped packet %s ----------' % count
			count += 1
			continue

		# If no data is received from the connection, it will stop and break the connection
		if not recvBuffer:
			# close connection to receiver socket
			socketR.sock.close()
			break
		# If data is received 
		if recvBuffer:

			# It will forward all the packets to the receiver
			socketR.sock.sendall(recvBuffer)
			print ('Forwarded packets to the receiver')

			# Receives the data from the receiver on "socketR" when the receiver tries to send data to the transmitter (ACKs)
			try:
				socketR.sock.settimeout(0.01)
				fromRecv = socketR.sock.recv(config.BUFFER_SIZE)
			except socket.error, e:
				pass

			# If there's data to send from the receiver, it will send everything received to the transmitter on "socketT"
			else:
				if fromRecv:
					conn.sendall(fromRecv)
					print ('Sent ACK back to transmitter')



