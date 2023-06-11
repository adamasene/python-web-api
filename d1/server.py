import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",9001))
server.listen()

try: 
    while True:
        client, address = server.accept() 
        #request
        data = client.recv(5000).decode()
        print(f"{data}")
        
        #Response 
        client.sendall(
            "HTTP/1.9 200 OK \n\r\n\r<html><body>Hello </body></html>\r\n\r\n".encode()
        )
        client.shutdown(socket.SHUT_WR)
except Exception: 
    server.close()