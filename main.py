from client.client_ssh import ClientSsh

snare = '192.168.100.166'
accesodi='143.0.100.230'
ssh_default_port = 22


def main():
    session = ClientSsh(accesodi,ssh_default_port,snare,ssh_default_port)
    session.get_connection()

if __name__ == "__main__":
    main()