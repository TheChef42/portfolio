import socket

#Import threading is a way to use threads in our python code
import threading

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def handle_client(clientConnection, clientAddress):
    print("Connected client:", clientAddress)

    while True:
        data = clientConnection.recv(1024).decode()
        if not data:
            break
        print(f"Received from {clientAddress}: {data}")

        if data == 'bye':
            clientConnection.send('Goodbye!'.encode())
            break
        elif data.isdigit():
            number = int(data)
            if is_prime(number):
                clientConnection.send(f"{number} is a prime number.".encode())
            else:
                clientConnection.send(f"{number} is not a prime number.".encode())
        else:
            clientConnection.send("Invalid input. Please send an integer number or 'bye' to exit.".encode())

    clientConnection.close()
    print(f"Connection with {clientAddress} closed.")

def handle_client2(clientConnection, clientAddress):
    data = clientConnection.recv(1024).decode()
    print(f"Received from {clientAddress}: {data}")
    client.send(data.encode())
    response = client.recv(1024).decode()
    clientConnection.send(response.encode())

# Constants
LOCALHOST = "127.0.0.1"
PORT = 12345

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(10)
print("Server started")
print("Waiting for client requests...")

SERVER2 = "127.0.0.1"
PORT2 = 12347
# Making a socket instance
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect to the server
client.connect((SERVER2, PORT2))

counter = 0


while True:
    clientConnection, clientAddress = server.accept()
    ############################# Insert your code here #############################
    # Use this logic: Declare the thread, then just start it.

    if counter == 2:
        t2 = threading.Thread(handle_client2(clientConnection, clientAddress))
        t2.start()
        counter = 0
        continue

    t1 = threading.Thread(target=handle_client(clientConnection, clientAddress), name="1")
    t1.start()
    counter += 1

