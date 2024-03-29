import socket

# IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = ('localhost', PORT)
SIZE = 1024
FORMAT = "utf-8"

def receive_message(socket):
    data = socket.recv(SIZE).decode(FORMAT)
    return data.split('\r\n\r\n', 1)

def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    """ Server has accepted the connection from the client. """
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    """ Receiving the filename from the client. """
    filename = conn.recv(SIZE).decode(FORMAT)
    
    print(f"Receiving the filename for create")
    file = open(f"data/{filename}", "w")
    conn.send("Filename received.".encode(FORMAT))

    """ Receiving the file data from the client. """
    request = receive_message(conn)
    headers, body = request
    print(f"status code: {headers.split()[1]}\nstatus pharse: {headers.split()[2]}")
    file.write(body)
    conn.send("File data received".encode(FORMAT))

    """ Closing the file. """
    file.close()

    """ Closing the connection from the client. """
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()