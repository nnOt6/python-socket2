from socket import *
from datetime import datetime
import threading
import time

HOST = "127.0.0.1"
PORT = 4546
BUFSIZE = 4096
ADDRESS = (HOST, PORT)
cs = socket(AF_INET, SOCK_STREAM)
threadLock = threading.Lock()
unc = 'UTF-8'
try:
    cs.connect(ADDRESS)
except socket.error as e:
    print("HAVE ERROR: " + str(e) + "...")


while True:
    print(" - Lobby - ")
    allMenu = "[1] cal_power\n[2] cal_triangle\n[3] cal_rectangle\n\
[4] cal_rhombus\n[5] cal_cubic\n[6] cal_sphere\n[7] getAerage\n\
[8] cal_lineDistance\n[9] cal_cone\n[10] getSum\nSelect Menu:"
    menu = input(allMenu)
    if menu == "1":
        send_menu = "1#1#pow"
    elif menu == "2":
        send_menu = "1#2#triangle"
    elif menu == "3":
        send_menu = "1#3#rectangle"
    elif menu == "4":
        send_menu = "1#4#rhombus"
    elif menu == "5":
        send_menu = "1#5#cubic"
    elif menu == "6":
        send_menu = "1#6#sphere"
    elif menu == "7":
        send_menu = "1#7#getAerage"
    elif menu == "8":
        send_menu = "1#8#lineDistance"
    elif menu == "9":
        send_menu = "1#9#cone"
    elif menu == "10":
        send_menu = "1#10#getSum"
    else:
        continue
    cs.send(bytes(send_menu,unc))

    ptcmenu = bytes.decode(cs.recv(BUFSIZE),unc).strip().split('#')
    data1, code, data3 = ptcmenu[0], ptcmenu[1], ptcmenu[2]

    #4
    if code == "1":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('base :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            b = int(input('exp  :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))            
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)
    #5
    elif code == "2":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('high :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            b = int(input('base :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))            
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)

    #6        
    elif code == "3":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('width :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            b = int(input('high :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))            
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print(result)
    #7        
    elif code == "4":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('width :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            b = int(input('high :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))            
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)             

    #8     
    elif code == "5":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('side :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)

    #9
    elif code == "6":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('side :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)

    #16
    elif code == "7":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('n :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)

    #11
    elif code == "8":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('A :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            b = int(input('B :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))
            else:
                print("Please input number!")
                continue            
            
            c = int(input('C :'))
            if c == 999:
                cs.send(str.encode(str(c),unc))
                break
            elif type(c) is int:
                cs.send(str.encode(str(c),unc))
            else:
                print("Please input number!")
                continue
            
            d = int(input('x1 :'))
            if d == 999:
                cs.send(str.encode(str(d),unc))
                break
            elif type(d) is int:
                cs.send(str.encode(str(d),unc))
            else:
                print("Please input number!")
                continue            
            
            e = int(input('y1 :'))
            if e == 999:
                cs.send(str.encode(str(e),unc))
                break
            elif type(e) is int:
                cs.send(str.encode(str(e),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)
            
    #10
    elif code == "9":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('high :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            b = int(input('radius :'))
            if b == 999:
                cs.send(str.encode(str(b),unc))
                break
            elif type(b) is int:
                cs.send(str.encode(str(b),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)

    #20
    elif code == "10":
        print("\n999 = Exit to Lobby")
        while True:
            a = int(input('n :'))
            if a == 999:
                cs.send(str.encode(str(a),unc))
                break
            elif type(a) is int:
                cs.send(str.encode(str(a),unc))
            else:
                print("Please input number!")
                continue
            
            result = bytes.decode(cs.recv(BUFSIZE),unc)
            print("result = ",result)
    #
    else:
        pass
    
cs.close()





    
