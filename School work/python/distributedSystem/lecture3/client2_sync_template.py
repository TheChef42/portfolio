import socket
#Import threading to use threads in our python code
import threading
import random
import time

numbers = [(random.randint(1, 100)), (random.randint(1, 100)), (random.randint(1, 100)), (random.randint(1, 100)), (random.randint(1, 100))]


def client_thread():
    SERVER = "127.0.0.1"
    PORT = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    global numbers
    try:
        print(numbers)
        while (True):
            index = random.randint(0, 4)
            if numbers[index] < 0:
                continue
            else:
                number = str(numbers[index])
                break

        client.send(number.encode())
        response = client.recv(1024).decode()
        print(f"Server Response: {response}\n")
        numbers[index] = -1
        #time.sleep(5)  # Add a 5-second delay to see the response
    finally:
        client.close()

def main():

    # Get input for the number of clients to initiate.

    num_clients = int(input("Enter the number of clients to initiate: "))
    global numbers

    # Create an empty list that we will append later on to carry the threads
    client_threads = []
    # We are not interested in how many times the loop will be run, but it will be run a specific amount of times (input) so use for _
    for _ in range(num_clients):
        # Declare the thread
        thread = threading.Thread(target=client_thread)
        # Append the list
        client_threads.append(thread)
        #Start the thread
        thread.start()

    # Wait for all client threads to finish
    for thread in client_threads:
        thread.join()

if __name__ == "__main__":
    main()
