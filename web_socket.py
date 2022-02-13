import socket

from datetime import *


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 12003

# Create socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#making socket available as fast as possible #### reserving port 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# this bind socked to a specific interface
server_socket.bind((SERVER_HOST, SERVER_PORT))

# inviting connection from else where, which is listning 
server_socket.listen(1)
print('Listening on port: ...' ,SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request  --- receiving data 
    request = client_connection.recv(1024).decode()
    print(request)

    # Parce header to get content of html
    headers = request.split('\r\n')
    filename = headers[0].split()[1]
    #print(' ')
    #print(headers)
    #print(filename)
    
    # Wrinting request to a file   ## Making logs
    ip = headers[1].split(':')[1]
    date=datetime.now()
    logs="REQUESTED_IP:{}, - -[{}] {}\n".format(ip,date,headers[0])

    with open("log.txt", 'a') as making_log_file:
        making_log_file.write(logs)  
    
    
    # Get the content of the files
    if filename == '/' or filename== '/index.html':
        filename = 'docs/index.html'

    elif filename=='/test.html':
        filename = 'docs/test.html'

    else:
        filename='docs/404.html'
    
    #read from the docs file
    file_object = open(filename,'r')
    content = file_object.read()
    file_object.close()
    
    # Return an HTTP response
    response='HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()

