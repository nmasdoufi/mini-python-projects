'''
How does a port scanner Works ?

It sends a network request to connect to a specific TCP or UDP port on a computer and records the response.

'''

import pyfiglet # takes an ascii text and renders it in ascii art fonts
import sys
import socket
from datetime import datetime

# Let's make the Entry cool 
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Let's make sure that the user types a valid amount of arguments
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    # gethostbyname translates a host name to IPv4 format, the IPv4 address is returned as a string.
else:
    print("Please enter an IP address.")    

print("-"*50)
print("Scanning the Target : "+ target)
print("Scanning started at : "+ str(datetime.now()))
print("-"*50)

try:
    for port in range(1,100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET ==> IPv4, SOCK_STREAM ==> TCP
        # socket.setdefaulttimeout(1) # After 1 second the port is considered close

        result = sock.connect_ex((target, port))
        if result == 0:
            print("[+] Port {} is open.".format(port))
        sock.close()

except KeyboardInterrupt:
    print("\nExiting the Program ...")
    sys.exit()
except socket.gaierror:
    print("\nHostname could'nt be Resolved.")
    sys.exit()
except socket.error:
    print("\nServer is'nt Responding.")
    sys.exit()

print("-"*50)
print("Scanning terminated at : "+ str(datetime.now()))
print("-"*50)    