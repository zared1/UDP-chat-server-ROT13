import socket
import string

def rot13(msg):
    trans_table = msg.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                    string.ascii_uppercase[13:] + string.ascii_uppercase[:13])

    enc_msg = message.translate(trans_table)

    return enc_msg

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 10001))

    print("CommServer initiated on port 10001. Prepare for incoming enemies.")

    while True:
        data, addr = sock.recvfrom(1024)
        msg data.decode()
        print(f"Discovered a transmission from {addr}: {msg}")
        
        response = input("Speak now:)
        enc_response = rot13(response)
        sock.sendto(encoded_response.encode(), addr)

if __name__ == '__main__':
    main()
