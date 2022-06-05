import socket
import termcolor


def scan_port(ipaddress,port):
	try:
		sock = socket.socket()  #creating object for socket#
		sock.connect((ipaddress,port)) #establishing a connection and if the port is open the connection will be suceessfull else it will go to except part#
		print("port open "+str(port))
		sock.close()
	except:
		print("port close "+str(port))

def scan(target,port):
	for ports in range(1,port):
		scan_port(target,ports)


target=input("Enter the IP Address of the targets by separating by ',': ")
n=int(input("Enter how many ports to be scanned: "))
if ',' in target:
	for ipadd in target.split(','):
		scan(ipadd.strip(' '),n)
else:
	scan(target,n)
