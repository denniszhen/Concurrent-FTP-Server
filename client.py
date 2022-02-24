import os
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 34242
ADDR = (IP, PORT)  # tuple
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DISCONNECTED":
            print(f"{msg}")
            break

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))  # send formatted command to server
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))  # send formatted command to server
            break
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))  # send formatted command to server
        elif cmd == "UPLOAD":

            # UPLOAD@filename@text
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()

            ## [data, client_data, data.txt]
            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            # send formatted command to server
            client.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            # send formatted command to server
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))

    print("Disconnected from the server.")
    client.close()


if __name__ == "__main__":
    main()
