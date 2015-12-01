############################################
# File name: MySocket class (mySocket.py)  #                  
# Author: Jackie Ye & Reymon Mercado       #              
# Assignment: FINAL PROJECT for COMP 7005  #                 
# Instructor: Aman Abdulla                 #    
############################################

import socket

class mysocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def mysend(self, msg, buflen):
        totalsent = 0
        while totalsent < buflen:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self, buflen):
        chunks = []
        bytes_recd = 0
        while bytes_recd < buflen:
            chunk = self.sock.recv(min(buflen - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)