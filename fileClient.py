import socket

def Main():
	host = '127.0.0.1'
	port = 5015

	s = socket.socket()
	s.connect((host,port))

	fileName = input("fileName : ")

	if fileName != 'q':
		s.send(fileName.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		if data[:6] == "Exists":
			fileSize = data[6:]
			message = input("File Exists "+str(fileSize)+"dwld (y/n):")
			if(message == 'y'):
				s.send(('OK').encode('utf-8'))
				f = open('new_'+fileName, 'wb')
				data = s.recv(1024)
				totalRecv = len(data)
				f.write(data)
				while(totalRecv < int(fileSize)):
					data = s.recv(1024)
					totalRecv += len(data)
					f.write(data)
					print(str((totalRecv/float(fileSize))*100)+"% done")

				print("Completed")
		else:
			print("doesnt Exists")
	s.close()

if __name__ == '__main__':
	Main()
