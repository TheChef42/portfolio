import socket
import threading, time

# Function to handle incoming messages from other peers
def receive_messages(client_socket, peer_name):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{peer_name}: {message}")
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to send messages to other peers
def send_message(client_socket):
    while True:
        message = input("Enter a message to send to other peers: ")
        client_socket.send(message.encode('utf-8'))

# Function to connect to other peers
def connect_to_peers(peers):
    for peer_name, host, port in peers:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to the peer
            time.sleep(5)
            client_socket.connect((host, port))
            print(f"Connected to {peer_name}")

            # Start two threads for sending and receiving messages with the remote peer
            receive_thread = threading.Thread(target=receive_messages, args=(client_socket, peer_name))
            send_thread = threading.Thread(target=send_message, args=(client_socket,))

            receive_thread.start()
            send_thread.start()

        except Exception as e:
            print(f"Error connecting to {peer_name}: {e}")

# Main function
def main():
    local_name = "LocalPeer"
    local_port = 12345

    peers = [("Peer0", "127.0.0.1", 12345),
             ("Peer1", "127.0.0.1", 12346),
             ("Peer2", "127.0.0.1", 12347),
             ("Peer3", "127.0.0.1", 12348),
             ("Peer4", "127.0.0.1", 12349)]

    local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_socket.bind(("127.0.0.1", local_port))
    local_socket.listen(1)

    print(f"{local_name} is listening on port {local_port}")

    # Start a thread to connect to other peers
    connect_thread = threading.Thread(target=connect_to_peers, args=(peers,))
    connect_thread.start()

    # Accept incoming connection from other peers
    while True:
        try:
            client_socket, client_addr = local_socket.accept()
            print(f"Connected to {client_addr}")

            # Start two threads for sending and receiving messages with the remote peer
            receive_thread = threading.Thread(target=receive_messages, args=(client_socket, local_name))
            send_thread = threading.Thread(target=send_message, args=(client_socket,))

            receive_thread.start()
            send_thread.start()

        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == "__main__":
    main()
