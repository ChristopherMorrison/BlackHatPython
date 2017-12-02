 
import socket

target_host = 'www.google.com'
target_port = 80

# [1] Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# [2] Connect to the Client
client.connect((target_host, target_port))

# [3] Send a GET request
client.send('GET / HTTP/1.1\r\n Host: google.com\r\n\r\n')

# [4] Receive the data returned
response = client.recv(4096)
print response

