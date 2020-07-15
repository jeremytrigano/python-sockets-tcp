#!/usr/bin/python3

import socket


def isprime(n):
    """check if integer n is a prime"""

    # negative numbers, 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the ony even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up the squareroot
    # of n for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


params = ("127.0.0.1", 8809)
BUFFER_SIZE = 1024  # default

data = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet, TCP
s.bind(params)
s.listen(1)

while True:
    conn, addr = s.accept()
    print("Connection accepted: %s" % str(addr))

    data = conn.recv(BUFFER_SIZE)
    if data == b"None\n":
        break
    print("Data received: %s" % data)
    try:
        number = int(data)
    except:
        response = b"E"
    else:
        if isprime(number):
            response = b"T"
        else:
            response = b"F"
    finally:
        conn.send(response)
        conn.close()
