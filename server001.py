import socket
import threading

ip = "0.0.0.0"
port = 5000

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conn.bind((ip,port))

conn.listen(5)

print("wating for connection on port:%d%s"%(port,"..."))

def connConnect(conn):

    data = list()

    client, addr = conn.accept()

    data.append(client)
    data.append(addr[0])
    data.append(addr[1])

    return data


def connSession(conn):

    client_messege = conn.recv(1024)

    print(client_messege)

    conn.send("ACK!")
        

def connTerminate(conn,port):

    #print(conn)
    #print(port)
    print("program has finished succefully, port %d is now open for reuse"%(port))

    conn.close()

def main():

    try:

        netdata = connConnect(conn)

        connSession(netdata[0])

        connTerminate(netdata[0],netdata[2])

    except socket.error as err:

        print(err)

        print("socket closed abruply")

main()
