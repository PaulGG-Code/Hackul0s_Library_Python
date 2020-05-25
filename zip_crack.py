import zipfile

host='192.168.46.145'

def iscorrect(passwordtotry):

    try:
        ziplavy=zipfile.ZipFile("claude.zip")
        ziplavy.extractall(pwd=passwordtotry)

    except:
        return False

    else:
        return True

f=open('password.dic','rb')
for word in f:
    print("trying password %s ..." %word.strip().decode())
    if iscorrect(word.strip()):
        print("Password found:", word.decode().strip())
        f.close()
        exit(0)
print("Password not found in your dictionary")
f.close()
