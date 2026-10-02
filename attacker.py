import socket

HOST = "127.0.0.1"
PORT = 5000          
REAL_SERVER_PORT = 5001 


def attack():
    print("=== ATTACK PROGRAM: Release of Message Contents ===")

   
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy.bind((HOST, PORT))
    proxy.listen(1)
    print(f"[ATTACKER] Waiting for client on {HOST}:{PORT}")

    client_conn, addr = proxy.accept()
    print(f"[ATTACKER] Client connected: {addr}")

    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((HOST, REAL_SERVER_PORT))
    print(f"[ATTACKER] Connected to real server on port {REAL_SERVER_PORT}")

    while True:
        data = client_conn.recv(1024)
        if not data:
            break

        
        print(f"[ATTACKER] >>> INTERCEPTED MESSAGE: {data.decode()}")

        
        server_sock.send(data)
        response = server_sock.recv(1024)
        client_conn.send(response)

    client_conn.close()
    server_sock.close()
    proxy.close()


if __name__ == "__main__":
    attack()
