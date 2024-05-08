# Multi User Chat Application

## Introduction
This documentation provides an overview of a simple chat application implemented in Python. The application consists of a server and a client component, allowing multiple users to communicate with each other in real-time over a network.

## Features
#### 1. Server Component:
- Listens for incoming client connections.
- Manages multiple client connections concurrently using threading.
- Supports sending and receiving messages.
- Allows private messaging between clients.
#### 2. Client Component:
- Provides a graphical user interface (GUI) for interacting with the chat room.
- Connects to the server to send and receive messages.
- Displays incoming messages from other users.
- Enables sending private messages to specific users.

## Architecture Overview
The chat application follows a client-server architecture:

#### Server:
- Implemented using Python's socket module.
- Listens for incoming connections on a specified IP address and port.
- Handles each client connection in a separate thread.
- Manages a dictionary of active clients, allowing broadcasting and private messaging.
#### Client:
- Implemented using Python's socket and Tkinter modules for GUI.
- Connects to the server using a TCP/IP socket connection.
- Provides a GUI window for user interaction, including entering username, sending messages, and displaying incoming messages.
- Utilizes threading to handle receiving messages from the server asynchronously.

## Usage
#### Starting the Server:
- Run the server.py script using Python 3.x.
- The server will start listening for connections on 127.0.0.1 and port 2048.
#### Connecting Clients:
- Run the client.py script using Python 3.x.
- Enter a username and click the "Connect" button.
- The client GUI window will open, allowing interaction with the chat room.
#### Interacting in the Chat Room:
- To send a message to the chat room, type the message in the input box and press "Send".
- To send a private message to a specific user, type @username message in the input box and press "Send".
- Incoming messages from other users will be displayed in the chat window.

## Error Handling
The application includes error handling mechanisms to deal with connection issues, malformed messages, and other exceptions that may occur during execution.

## Notes
- The chat application is designed for demonstration purposes and may require further enhancements for scalability, security, and robustness in a production environment.
- It is recommended to run the server and client on the same local network for optimal performance and reliability.

## Dependencies
- Python 3.x
- Tkinter (for the client GUI)

## Limitations
- The application currently lacks authentication and authorization mechanisms.
- Error handling may be further improved to handle edge cases and unexpected scenarios.
- The user interface may not be optimized for all screen sizes and resolutions.

## Contributions
Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the project repository.
