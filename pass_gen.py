import random

#Characters
s="abcdefghijklmnopkrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_.{}[];"

#Setting the password Length
passwordlen = 18

#Generate the password
password = "".join(random.sample(s,passwordlen))

#Print the password 
print(password)
