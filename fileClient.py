import socket
import threading


def getFile(name,s):
	#print(data)
	data = s.recv(1024).decode('utf-8')
	if data[:3] != 'ERR':
		fileSize = data[7:]
		#message = input("y/n : ")
		message = 'y'
		if(message == 'y'):
			#fileName = input("FileName?:")
			fileName = 'fileName.py'
			s.send(('OK').encode('utf-8'))
			f = open(fileName, 'wb')
			data = s.recv(1024)
			totalRecv = len(data)
			f.write(data)
			print(totalRecv)
			while(totalRecv < int(fileSize)):
				data = s.recv(1024)
				totalRecv += len(data)
				f.write(data)
				print(str((totalRecv/float(fileSize))*100)+"% done")
			print("Completed")
	else:
		print("doesnt Exists")
	s.close()


def Main():
	host = '192.168.3.153'
	port = 5015
	s = socket.socket()
	s.connect((host,port))

	while(1):
		send = input('Send y/n : ')
		if(send == 'y'):
			t = threading.Thread(target = getFile, args = ("getFile",s))
			t.start()
		print("In main")

if __name__ == '__main__':
	Main()
