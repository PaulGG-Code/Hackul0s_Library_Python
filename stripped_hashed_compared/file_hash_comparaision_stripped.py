import hashlib
import sys


f1=sys.argv[1]
f2=sys.argv[2]

ff=open(f1,'rb')
data=ff.read()

fs=open(f2, 'rb')
data2=fs.read()

#stripping / removing spaces from before and after

data=data.decode().strip("\n").strip().encode()
data2=data2.decode().strip("\n").strip().encode()

claude1=hashlib.sha256(data)
print(claude1.hexdigest())

claude2=hashlib.sha256(data2)
print(claude2.hexdigest())
