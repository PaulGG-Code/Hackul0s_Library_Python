import pikepdf


def iscorrect(passwordtotry):

    try:
        pikepdf.open('paul.pdf',passwordtotry)

    except:
        return False

    else:
        return True

f=open('password.dic','r')
for word in f:
    print("trying password %s" %word.strip())

    if iscorrect(word.strip()):
        print("Password found:", word.strip())
        f.close()
        exit(0)

print("Password not found in your dictionary")
f.close()
