############################################
# File name: MyPacket class (myPacket.py)  #                  
# Author: Jackie Ye & Reymon Mercado       #              
# Assignment: FINAL PROJECT for COMP 7005  #                 
# Instructor: Aman Abdulla                 #    
############################################

class mypacket:

	def __init__(self, p_type, seqNum, data, winSize, ackNum):
		# type 1=ACK, 2=Data, 3=EOT
		self.type = p_type
		self.seqNum = seqNum
		self.data = data
		self.winSize = winSize
		self.ackNum = ackNum

