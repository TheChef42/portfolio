# Import socket module
import socket

# In this Line we define our local host
# address with port number
SERVER = "127.0.0.1"
PORT = 12345
# Making a socket instance
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER, PORT))

# Running a infinite loop
while True:
    message = input("Enter a number or 'bye' to exit: ")
    client.send(message.encode())

    if message == 'bye':
        print(client.recv(1024).decode())
        break

    response = client.recv(1024).decode()
    print("Server:", response)

client.close()
