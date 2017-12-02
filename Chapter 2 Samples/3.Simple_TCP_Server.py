# [1] Same as the clients, we build this by using socket
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# [2] Start listening for connections over the specified ip and port
server.bind((bind_ip,bind_port))
server.listen(5)
print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# [3] This is our client-handling thread
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request

    # send back a packet
    client_socket.send("ACK!")
    client_socket.close()

# [4] Recieve connections and handle them
while True:
    client, addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    
    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
