import time, sys
import socket
import colorama
import os

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print(colorama.Fore.BLUE + "[" + colorama.Fore.RED + "*" + colorama.Fore.BLUE + "]" + colorama.Fore.RESET + " Connected With: " + colorama.Fore.CYAN + s_ip + colorama.Fore.RESET)

name = colorama.Fore.RED + os.getcwd() + colorama.Fore.GREEN + "> " + colorama.Fore.BLUE
print(name)

new_socket.listen(1)

conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ', add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected.')

conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
