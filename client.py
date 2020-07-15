#!/usr/bin/python3


import socket

params = ("127.0.0.1", 8809)
BUFFER_SIZE = 1024  # default

numbers = [4, 5, -5, 17, 29, 2 ** 50, 2 ** 50 - 1]

for number in numbers:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(params)
    print("Send message %s" % number)
    s.send(("%s\n" % number).encode("utf8"))
    data = s.recv(BUFFER_SIZE)
    if len(data) == 0:
        print("\tNo response")
    elif data == b"E":
        print("\tServer error")
    elif data == b"T":
        print("\tNumber %s is a prime number" % number)
    elif data == b"F":
        print("\tNumber %s is not a prime number" % number)
    else:
        print("\tWrong data sent: %s" % data)
    s.close()

# Send end of message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(params)
s.send(("%s\n" % None).encode("utf8"))
s.close()

