

class MyPacket:

	def __init__(self, p_type, seqNum, data, winSize, ackNum):
		self.type = p_type
		self.seqNum = seqNum
		self.data = data
		self.winSize = winSize
		self.ackNum = ackNum

