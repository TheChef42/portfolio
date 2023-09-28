# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 80

# connect to the server on local computer
s.connect(('10.92.1.134', port))

# receive data from the server and decoding to get the string.
msg =""

while(msg != "bye"):
    while True:
        try:
            msg = input("Send int to test or bye to stop:")
            if msg == "bye":
                break
            int(msg)
            break
        except:
            print("Not valid option!")
    s.send(msg.encode())
    msg = s.recv(1024).decode()
    print(msg)



# close the connection
s.close()



