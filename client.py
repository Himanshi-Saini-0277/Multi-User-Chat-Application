import tkinter as tk
from tkinter import ttk
import socket
import threading

HOST = '127.0.0.1'
PORT = 2048

class ClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None

        self.top_frame = ttk.Frame(self.root)
        self.top_frame.pack(fill=tk.BOTH, expand=True)
        self.label_username = ttk.Label(self.top_frame, text="Enter Username:")
        self.label_username.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry_username = ttk.Entry(self.top_frame)
        self.entry_username.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_connect = ttk.Button(self.top_frame, text="Connect", command=self.connect)
        self.button_connect.pack(side=tk.LEFT, padx=5, pady=5)

        self.middle_frame = ttk.Frame(self.root)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)
        self.text_messages = tk.Text(self.middle_frame, state=tk.DISABLED)
        self.text_messages.pack(fill=tk.BOTH, expand=True)

        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)
        self.entry_message = ttk.Entry(self.bottom_frame)
        self.entry_message.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.entry_message.bind("<Return>", self.send_message)
        self.button_send = ttk.Button(self.bottom_frame, text="Send", command=self.send_message)
        self.button_send.pack(side=tk.LEFT, padx=5, pady=5)

    def connect(self):
        username = self.entry_username.get().strip()
        if username:
            try:
                self.client_socket.connect((HOST, PORT))
                self.client_socket.sendall(username.encode('utf-8'))
                threading.Thread(target=self.receive_messages).start()
                self.username = username
                self.entry_username.config(state=tk.DISABLED)
                self.button_connect.config(state=tk.DISABLED)
            except Exception as e:
                print(f"Unable to connect to server - {HOST} - {PORT}")
                print(e)
                
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(2048).decode('utf-8')
                self.text_messages.config(state=tk.NORMAL)
                self.text_messages.insert(tk.END, message + "\n")
                self.text_messages.see(tk.END)
                self.text_messages.config(state=tk.DISABLED)
            except Exception as e:
                print(e)
                break

    def send_message(self, event=None):
        message = self.entry_message.get().strip()
        if message:
            if message.startswith('@'):
                self.send_private_message(message)
            else:
                self.client_socket.sendall(message.encode('utf-8'))
            self.entry_message.delete(0, tk.END)

    def send_private_message(self, message):
        recipient_username, private_message = message.split(' ', 1)
        recipient_username = recipient_username[1:]
        private_message = f"/pm {recipient_username} {private_message}"
        self.client_socket.sendall(private_message.encode('utf-8'))

def main():
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
