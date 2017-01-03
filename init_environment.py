
import socket
import os
import subprocess
import re


TANNER_LOCATION = "/opt/tanner/bin"
TANNER_PORT = 8090
ports=['8090','8090']

def kill_process():
    popen = subprocess.Popen(['netstat', '-lpn'],
                         shell=False,
                         stdout=subprocess.PIPE)
    (data, err) = popen.communicate()

    pattern = "^tcp.*((?:{0})).* (?P<pid>[0-9]*)/.*$"
    pattern = pattern.format(')|(?:'.join(ports))
    prog = re.compile(pattern)
    for line in data.split('\n'):
        match = re.match(prog, line)
        if match:
            pid = match.group('pid')
            subprocess.Popen(['kill', '-9', pid])

def check_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',TANNER_PORT))
    if result == 0:
        print "El puerto esta en uso"
        kill_process()
        print "El proceso fue matado con exito"
   

def main():
    os.chdir(TANNER_LOCATION)
    
    if not check_port():
        status=os.system(" python3.5 tanner  --config pepe" )
        print status

main()
        

    
