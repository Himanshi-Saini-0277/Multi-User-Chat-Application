import socket
import threading

HOST = '127.0.0.1'
PORT = 2048
LISTENER_LIMIT = 5
active_clients = {}

def handle_client(client_socket, client_address):
    try:
        username = client_socket.recv(2048).decode('utf-8')
        print(f"Successfully connected to {username} - {client_address[0]} - {client_address[1]}")
        client_socket.sendall("Welcome to the chat!".encode())

        active_clients[username] = client_socket
        
        broadcast_join_message(username)

        while True:
            message = client_socket.recv(2048).decode('utf-8')
            if message:
                if message.startswith('/pm'):
                    send_private_message(username, message)
                else:
                    broadcast_message(username, message)
    except ValueError:
        print("Error: Received malformed message")
    except Exception as e:
        print(f"Error: {e}")

def send_private_message(sender_username, message):
    recipient_username, private_message = message.split(' ', 2)[1:]
    recipient_username = recipient_username.strip()
    
    recipient_socket = active_clients.get(recipient_username)
    
    if recipient_socket:
        private_message = f"{sender_username} [private] ~ {private_message}"
        recipient_socket.sendall(private_message.encode('utf-8'))
        print("Private message sent to:", recipient_username)
    else:
        print("Recipient not found.")

def broadcast_join_message(username):
    join_message = f"{username} joined the chat."
    print(join_message)
    for socket in active_clients.values():
        socket.sendall(join_message.encode())

def remove_client(username):
    if username in active_clients:
        del active_clients[username]

def broadcast_message(sender_username, message):
    broadcast_msg = f"{sender_username} ~ {message}"
    print(broadcast_msg)
    for socket in active_clients.values():
        socket.sendall(broadcast_msg.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on - {HOST} - {PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}")
        print(e)
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client_socket, client_address = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    main()
