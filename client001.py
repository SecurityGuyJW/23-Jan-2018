#the most basic kind of client your can make

import socket

netdata = list()

ip = "192.168.237.155"
port = 5000
conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

netdata.append(conn)
netdata.append(ip)
netdata.append(port)


def connConnect(netdata):

    try:
        netdata[0].connect((netdata[1],netdata[2]))

    except socket.error as err:
        print(err)
        print("connection has failed...")
        print("port:",netdata[2]," is now open")
        netdata[0].close()

def connSession(netdata):
    netdata[0].send("SYN!")

    server_response = netdata[0].recv(1024)

    print(server_response)

def connTerminate(netdata):
    netdata[0].close()

def main():

    connConnect(netdata)
    connSession(netdata)
    connTerminate(netdata)

main()