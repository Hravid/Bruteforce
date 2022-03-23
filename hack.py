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

    n = 1
    while True:
        file = open('passwords.txt', 'r')
        for password in file:
            ans = list(map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()]for letter in password))))

            # send message

            for word in ans:
                message = word.encode(encoding='utf-8')
                client_socket.send(message)

                # receive response

                response = client_socket.recv(1024)
                response = response.decode(encoding='utf-8')

                if response == "Connection success!":
                    print(word)
                    break
            if response == "Connection success!":
                break
                file.close()
