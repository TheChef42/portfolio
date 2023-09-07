# first of all import the socket library
import socket
import math

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12344

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")


def is_prime_trial_division(n):
    # Check if the number is less than
    # or equal to 1, return False if it is
    if n <= 1:
        return False
    # Loop through all numbers from 2 to
    # the square root of n (rounded down to the nearest integer)
    for i in range(2, int(math.sqrt(n)) + 1):
        # If n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
    # If n is not divisible by any of these numbers, return True
    return True


# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    s.settimeout(5)
    msg = ""
    while msg != "bye":
        msg = c.recv(1024).decode()
        print(msg)
        if msg == "bye":
            break
        else:
            if is_prime_trial_division(int(msg)):
                msg = "Prime"
            else:
                msg = "Not Prime"
        c.send(msg.encode())

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    # Close the connection with the client
    c.close()
    # Breaking once connection closed
    break
