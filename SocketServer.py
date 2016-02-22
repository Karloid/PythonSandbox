import socket

import sys

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('', 7000))
except socket.error as msg:
    print msg
    sys.exit()

s.listen(10)
while True:
    conn, addr = s.accept()
    print "New Connection! from " + str(addr)
    data = conn.recv(1024)
    line = data.decode('UTF-8')
    line = line.replace("\n", "")
    conn.send("lol\n\r")
    conn.send("BzzIsPerfect")
    conn.send("current time is " + str(time.time()))
    conn.close()
    print line

s.close()
