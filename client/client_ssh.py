import paramiko
hostname = "accesodi.iua.edu.ar"
port = 22
username="salasia"
password="devjava@530240"
nbytes = 12500
class ClientSsh:
    def __init__(self,jumping_ip,jumping_port,vm_ip,vm_port):

        self.jumping_ip = jumping_ip
        self.jumping_port = jumping_port
        self.vm_ip=vm_ip
        self.vm_port = vm_port

    def get_connection(self):

        jumping_server = paramiko.SSHClient()
        jumping_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumping_server.connect(hostname, username=username, password=password)
        jumping_channel = jumping_server.get_transport()
        dest_vm_address = (self.vm_ip, self.vm_port)
        local_addr = (self.jumping_ip, self.jumping_port)
        vmchannel = jumping_channel.open_channel("direct-tcpip", dest_vm_address, local_addr)

        vm_client=paramiko.SSHClient()
        vm_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        k = paramiko.RSAKey.from_private_key_file( filename="/home/santi/tesis/2017/tesis")

        vm_client.connect(hostname='192.168.100.166', username='root', pkey=k, sock=vmchannel)
        print "connected"

        stdin,stdout,error =vm_client.exec_command("python tesis-scripts/init_environment.py")
        print stdout.read()



    def close_session(self):
        self.session.close()
        self.jumping_session.close()



