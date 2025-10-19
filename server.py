import socket
import string

def rot13(msg):
    trans_table = msg.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )
    enc_msg = msg.translate(trans_table)
    return enc_msg

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 10001))

    print("UDP ROT13 Chat Server initiated on port 10001. Ready for incoming messages.")

    while True:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        print(f"Received from {addr}: {msg}")

        response = input("Server response: ")
        enc_response = rot13(response)
        sock.sendto(enc_response.encode(), addr)

if __name__ == '__main__':
    main()
