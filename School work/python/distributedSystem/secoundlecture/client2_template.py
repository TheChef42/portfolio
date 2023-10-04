import socket
# Import threading to use threads in our python code
import threading
import random
import time


def client_thread():
    SERVER = "127.0.0.1"
    PORT = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    try:
        number = random.randint(1, 100)
        client.send(str(number).encode())
        response = client.recv(1024).decode()
        print(f"Server Response: {response}")
        #time.sleep(5)  # Add a 5-second delay to see the response
    finally:
        client.close()


def main():
    numberClients = int(input("How many clients do you want?:  "))
    # Get input for the number of clients to initiate.
    threadLists = list()
    # Create an empty list that we will append later on to carry the threads
    for _ in range(numberClients):
        t = threading.Thread(target=client_thread(),)
        threadLists.append(t)
        t.start()

    for t in threadLists:
        t.join()



    # We are not interested in how many times the loop will be run, but it will be run a specific amount of times (input) so use for _

    # Declare the thread

    # Append the list

    # Start the thread

    # Wait for all client threads to finish


if __name__ == "__main__":
    main()
