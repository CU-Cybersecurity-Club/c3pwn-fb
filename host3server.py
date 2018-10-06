import socket
import sys
import random
from time import sleep

port = 5500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',port))

print("Listening on port 5500")
while True:
    routes = {'2000':0,'2001':0,'2004':0,'2005':0,'2003':0,'3003':0}
    while True:
        #rand = random.randint(0,10)
        message, address = sock.recvfrom(1024)
        #print("data sent is: {}".format(message))
        #print("Address: {}".format(address))
        p = address[1]
        if(p == 10000 or p == 20000 or p == 30000 or p == 40000 or p == 50000):
            break
        elif(address[1] == 2000):
            routes[str(address[1])] += 1
            #print("count for port 2000: {}".format(routes[str(address[1])]))
        elif(address[1] == 2001):
            routes[str(address[1])] += 1
            #print("count for port 2001: {}".format(routes[str(address[1])]))
        elif(address[1] == 2004):
            routes[str(address[1])] += 1
            #print("count for port 2004: {}".format(routes[str(address[1])]))
        elif(address[1] == 2005):
            routes[str(address[1])] += 1
            #print("count for port 2005: {}".format(routes[str(address[1])]))
        elif(address[1] == 2003):
            routes[str(address[1])] += 1
            #print("count for port 2003: {}".format(routes[str(address[1])]))
        elif(address[1] == 3003):
            routes[str(address[1])] += 1
            #print("count for port 3003: {}".format(routes[str(address[1])]))

#    elif(address[1] ==
#    for i in range(len(routes)):
#        print("There is {}% loss for route {}".format((1-routes[i]/total)*100,i))
    sums = {'2000':1000,'2001':1000,'2004':1000,'2005':1000,'2003':1000,'3003':1000}
    for i in routes:
        sums[i] = 1-(routes[i]/sums[i])
    print("Finished. all routes percentage of packets lost is {}".format(sums))
    for i in range(6):
        sock.recv(1024)