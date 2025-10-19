# UDP Chat Server (ROT13)

This project is a UDP-based chat server that encodes outgoing messages using the ROT13 cipher. It allows receiving messages from clients and sending encrypted responses interactively from the server console.

## Features

* Uses UDP sockets (`socket.SOCK_DGRAM`)
* Receives messages from clients and prints them in the console
* Outgoing messages are ROT13-encoded before being sent
* Demonstrates networking + simple cryptography in Python

## How to Run

1. Clone or download the repository.
2. Run the server script:

```bash
python server.py
```

3. Connect with a UDP client (e.g., `nc`/netcat):

```bash
nc -u localhost 10001
```

4. Type messages in the client to send them to the server.
5. Type messages in the server console — they will be ROT13-encoded before sending to the client.
