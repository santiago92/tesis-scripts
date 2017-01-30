from client.client_ssh import ClientSsh
import threading
import time
import os
snare = '192.168.100.166'
accesodi='143.0.100.230'
ssh_default_port = 22

def init_server():
    session = ClientSsh(accesodi, ssh_default_port, snare, ssh_default_port)
    session.get_connection()

def worker():
    print "inicializando hilo local"


def main():
    server= threading.Thread(name="server",target=init_server)
    local = threading.Thread(name='worker', target=worker)
    server.start()
    time.sleep(3)
    local.start()

if __name__ == "__main__":
    main()