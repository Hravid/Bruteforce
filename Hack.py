# write your code here
import socket
import sys
import itertools


args = sys.argv


with socket.socket() as client_socket:
    host = args[1]
    port = int(args[2])

    address = (host, port)

    # establish connection
    client_socket.connect(address)

    list_ = "abcdefghijklmnopqrstuvwxyz0123456789"
    n = 1
    while True:
        password = itertools.product(list_, repeat=n)

        # send message
        for i in password:
            word = "".join(i)

            message = word.encode()
            client_socket.send(message)

            # receive response

            response = client_socket.recv(1024)
            response = response.decode()

            if response == "Connection success!":

                print(word)
                break
        if response == "Connection success!":
            break
        n += 1

