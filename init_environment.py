
import socket
import os
TANNER_LOCATION = "/opt/tanner/bin"
TANNER_PORT = 8090
def check_port():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',TANNER_PORT))
    if result == 0:
        return True
    return False
   

def main():
    os.chdir(TANNER_LOCATION)
    
    if !check_port():
        status=os.system(" python3.5 tanner  --config pepe" )
        println status

main()
        

    
