import socket

# IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = ('localhost', PORT)
FORMAT = "utf-8"
SIZE = 1024
headers = {'Content-type': 'text/file'}

def send_message(socket, status_code, status_phrase, headers, body):
    message = f"Bosskung {status_code} {status_phrase}\r\n"
    for header, value in headers.items():
        message += f"{header}: {value}\r\n"
    message += f"\r\n{body}"
    socket.sendall(message.encode(FORMAT))

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Opening and reading the file data. """
    file = open("data/yt.txt", "r")
    data = file.read()

    """ Sending the filename to the server. """
    client.send("yt.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)

    """ Sending the file data to the server. """
    send_message(client, 200, 'OK', headers, data)
    # client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    client.close()

if __name__ == "__main__":
    main()
