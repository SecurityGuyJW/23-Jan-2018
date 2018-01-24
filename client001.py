#*****************************************
#*This client was written jan/23/2018    *
#*By: Juan Wagner			 *
#*****************************************


import socket

def getIPandPort():

    net_data = list()

    IP = raw_input("Enter IP:")
    port = int(input("Enter Port:"))

    net_data.append(IP)
    net_data.append(port)

    return net_data

def start_connection(sock,data):

    try:
        sock.connect((data[0],data[1]))
        sock.send(bytes("client > Sup\n",))
	while True:
		msg = raw_input("client:")
		sock.send(bytes("client > "))
		sock.send(bytes(msg))
		sock.send(bytes("\n"))

        	var = sock.recv(4060)
		var = "server > " + var
		print(var)
        	
		
		if msg == "12345":
			break;

    except socket.error as err:
        print(err)
        sock.close()

def close_connection(sock,data):

    print("Client:",sock)
    print("Port:",data[0])
    print("IP:",data[1])
    print("connection closed")

    sock.close()


def main():

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    data = getIPandPort()

    start_connection(conn,data)

    close_connection(conn,data)

main()




