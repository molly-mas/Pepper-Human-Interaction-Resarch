import naoqi
import subprocess

#import paramiko
'''
def scp_file(hostname, username, password, local_path, remote_path):
   ssh=paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   print(password)
   ssh.connect(hostname, username=username, password=password)
   scp = SCPClient(ssh.get_transport())
   scp.get(remote_path, local_path)
   scp.close()
   ssh.close()
'''
# Example usage:
#scp_file("192.168.3.137", 'molly_mas', 'nao', '~/recordings/microphone/HelloPepper.wav', '~/')


#192.168.3.137

#User_Name= "molly_mas"
#Host_Name = "192.168.3.137"
#Password = 'nao'
#Port = 22

#client = paramiko.SSHClient()
#client.connect(hostname=Host_Name, port=Port, username= User_Name, password= Password)
#print "YOU ARE HERE"
#sftp_client = client.open_sftp()
#sftp_client.get("~/recordings/microphone/HelloPepper.wav","~")
#sftp_client.close()


#MOLLY LOOK INTO PYTHON SUBPROCESS!!!!!!!

'''ls = subprocess.call(['ls'])
print ls '''

#GOT MY KEY SET UP try w subprocess next time for scp!!!!
# DOES NOT WORK KEEP TRYING IDK WHY 
def get_file():
   result = subprocess.call(["scp","-v","nao@192.168.3.137:~/recordings/microphones/user_audio.wav","user_audio.wav"])
   
#move = subprocess.call("mv", "HiPepperTwo.wav", )
#other_opt = subprocess.call(["sftp","-v","nao@192.168.3.137","get", "~/recordings/microphones/HiPepper.wav","~/"])

# IT WORKSSSS!!!!!!!!!!!!!!!!!!!!!!!!