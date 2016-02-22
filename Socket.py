import socket

import sys

host = ''
port = 7000

print "Creating socket"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print "Failed to create socket"
    sys.exit()

print "Gettings remote IP address"
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname resolving error"
    sys.exit()

s.connect((remote_ip, port))

request = "GET /EMIGRATION/NKUZNECOW/nisp01.txt HTTP/1.0\r\n\r\n"
try:
    s.sendall(request)
except socket.error:
    print "send failed"
    sys.exit()

reply = None
while reply != "":
    reply = s.recv(4096)
    print reply
