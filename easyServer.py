from socket  import *
from threading import Thread
import threading
from datetime import datetime
import sys
import math 
import os

class clientHandler(Thread):
    def __init__(self, client, address):
        Thread.__init__(self)
        self._client = client
        self._address = address
        
    def run(self):
        while True:            
            ptcmenu = bytes.decode(self._client.recv(BUFSIZE),unc).strip().split('#')
            data1, code, data3 = ptcmenu[0], ptcmenu[1], ptcmenu[2]

            #choice 4
            if code == "1":
                self._client.send(bytes("1#1#pow",unc))
                while True:
                    a = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if a == 999:
                        break
                    b = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if b == 999:
                        break
                    
                    x = pow(a, b)
                    self._client.send(bytes(str(x),unc))

             #choice 5
            if code == "2":
                self._client.send(bytes("1#2#triangle",unc))
                while True:
                    high = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if high == 999:
                        break
                    base = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if base == 999:
                        break
                    
                    result = 0.5*high*base
                    self._client.send(bytes(str(result),unc))

             #choice 6
            if code == "3":
                self._client.send(bytes("1#3#rectangle",unc))
                while True:
                    width = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if width == 999:
                        break
                    high = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if high == 999:
                        break
                    
                    result = width*high
                    self._client.send(bytes(str(result),unc))

             #choice 7
            if code == "4":
                self._client.send(bytes("1#4#rhombus",unc))
                while True:
                    width = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if width == 999:
                        break
                    high = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if high == 999:
                        break
                    
                    result = width*high
                    self._client.send(bytes(str(result),unc))

             #choice 8
            if code == "5":
                self._client.send(bytes("1#5#cubic",unc))
                while True:
                    side = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if side == 999:
                        break
                    
                    result = side*side*side
                    self._client.send(bytes(str(result),unc))

             #choice 9
            if code == "6":
                self._client.send(bytes("1#6#sphere",unc))
                while True:
                    radius = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if side == 999:
                        break
                    
                    result = (pow(radius,3))*4/3
                    self._client.send(bytes(str(result),unc))

             #choice 16
            if code == "7":
                self._client.send(bytes("1#7#getAerage",unc))
                while True:
                    n = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if n == 999:
                        break
                    sumz = 0
                    n = n + 1
                    for i in range(n):
                        print(i)
                        sumz = sumz + i
                    print(sumz)
                    
                    result = sumz/(n-1)
                    self._client.send(bytes(str(result),unc))                    

             #choice 11
            if code == "8":
                self._client.send(bytes("1#8#lineDistance",unc))
                while True:
                    a = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if a == 999:
                        break
                    b = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if b == 999:
                        break
                    c = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if c == 999:
                        break
                    x1 = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if x1 == 999:
                        break
                    y1 = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if y1 == 999:
                        break
                    
                    result = ((a*x1)+(b*y1*1)+c)/(math.sqrt((pow(a,2))+(pow(b,2))))
                    self._client.send(bytes(str(result),unc))

             #choice 10
            if code == "9":
                self._client.send(bytes("1#9#cone",unc))
                while True:
                    high = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if n == 999:
                        break
                    radius = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if n == 999:
                        break
       
                    result = (1*(pow(radius,2)*high))/3
                    self._client.send(bytes(str(result),unc))

             #choice 20
            if code == "10":
                self._client.send(bytes("1#10#getSum",unc))
                while True:
                    n = int(bytes.decode(self._client.recv(BUFSIZE)))
                    if n == 999:
                        break
                    result = 0
                    for i in range(n+1):
                        result = result + i
                    self._client.send(bytes(str(result),unc)) 

            #
            else:
                pass       


unc = 'UTF-8'
HOST = "127.0.0.1"
PORT = 4546
BUFSIZE = 4096
MAX_CLIENT = 10
server = socket(AF_INET, SOCK_STREAM)
ADDRESS = (HOST, PORT)
server.bind(ADDRESS)
server.listen(MAX_CLIENT)
threadLock = threading.Lock()
CONNECTIONS_LIST = []
CONNECTIONS_LIST.append(server)


print("Chat server started!")
print("IP ", HOST,"PORT ", PORT)

while True:
    print("Waiting for a clients connect...")
    client, address = server.accept()
    print("New connected by [IP] :", address[0])
    
    threadLock.acquire()
    CONNECTIONS_LIST.append(client)
    threadLock.release()
    handler = clientHandler(client, address)
    handler.start()   

            
