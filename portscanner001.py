import socket
import socketserver
import sys
from datetime import datetime

#Ask for host to be scanned
remoteserver = input ("Enter the network to be scanned:")
remoteserverIP = socket.gethostbyname(remoteserver)

#Print a banner for scanning
print("_"*60)
print("Please wait, Scanning in Progress", remoteserverIP)
print("_"*60)

#Check for timestamp
t1 = datetime.now

#Error handling cases
try:
    for port in range (1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteserverIP, port))
        if result == 0:
            print("port {}  \t Open".format(port))
        elif result == 61:
            print("port {}  \t Rejected by host".format(port))
        else:
            print("port {}  \t Timed Out".format(port))
            sock.close()

except KeyboardInterrupt:
    print("You have pressed CTRL+R")
    sys.exit()
except socket.gaierror:
    print("Host couldn't be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to server:", remoteserverIP)
    sys.exit()

#Checking the time taken
t2 = datetime.now
total = t2 -t1
print("Total time taken for scanning the host:", total)
