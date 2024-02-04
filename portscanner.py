import socket
import socketserver
import sys
from datetime import datetime

#Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are able to scan
print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP) 
print ("_" * 60)

#Check at what time the scan started
t1 = datetime.now

#Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# Error handling for catching errors

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}:  \t Open".format(port))
        elif result == 61:
            print ("port {}:  \t Rejected by Host".format(port))
        else:
            print ("port {}:  \t Timed Out".format(port))
            sock.close()

except KeyboardInterrupt:
    print ("You pressed CTRL+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#Checking the time again

t2 = datetime.now()

#Calculates the time difference, to see how long it took to run the script
total = t2 - t1

#printing the information on screen
print ("Scanning Completed in:"), total

