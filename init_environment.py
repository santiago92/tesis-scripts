
import socket
import os
import subprocess
import re



TANNER_LOCATION = "/opt/tanner/bin"
SNARE_LOCATION = "/opt/snare"
TANNER_PORT = 8090
ports=['8090','8080']

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
    emulate_page= "admin.openbts.com"
    os.chdir(TANNER_LOCATION)
    
    if not check_port():
        status_tanner=os.system(" python3.5 tanner  --config pepe&" )
        os.system("bg" )
        if status_tanner == 0:
            print "El inicio de tanner fue exitoso. Iniciando Snare"
            os.chdir(SNARE_LOCATION)
            status_snare=os.system("python3.5 snare.py  --page-dir "+ emulate_page +" --tanner 127.0.0.1 --skip-check-version --auto-update False > /opt/log_snare.log")
            os.system("bg" )
        if status_snare==0:
            print "El sistema tanner-snare se inicio con exito"


        
main()
        

    
