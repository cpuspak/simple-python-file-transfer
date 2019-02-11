import socket
import threading
import os

def RetrFile(name, sock):
	#fileName = sock.recv(1024).decode('utf-8')
	fileName = input()
	if os.path.isfile(fileName):
		sock.send(("Sending " +str(os.path.getsize(fileName))).encode('utf-8'))
		userResponse = sock.recv(1024).decode('utf-8')

		if userResponse[:2] == 'OK':
			with open(fileName, 'rb') as f:
				bytesToSend = f.read(1024)
				sock.send(bytesToSend)
				while(bytesToSend != ''):
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)

	else:
		sock.send('ERR')
	sock.close()

def Main():
	host = '192.168.3.153'
	port = 5015

	s = socket.socket()
	#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(('',port))
	s.listen(5)

	print("server started...")

	while(1):
		c,addr = s.accept()
		print("Connected to ip : "+ str(addr))

		t = threading.Thread(target = RetrFile, args = ('retrThread', c))
		t.start()

	s.close()

if __name__ == '__main__':
	Main()





