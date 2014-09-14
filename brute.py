import hashlib,time,os,sys
from itertools import product

##def xselections(items,n):
##    try:
##        if n==0:
##            yield []
##        else:
##            for i in xrange(len(items)):
##                for ss in xselections(items,n-1):
##                    yield [items[i]]+ss
##    except(KeyboardInterrupt):
##        print "\n Received Ctrl+C, terminating...\n"
##        sys.exit()

numb=range(48,58)
cap=range(65,91)
low=range(97,123)
dig=range(33,65)
other=range(90,97)+range(122,128)
choice=0

def update(result):
    sys.stdout.write("\r%2s" % result)
    sys.stdout.flush()

try:
    while choice not in range(1,9):
        choice=raw_input('''
            1) Numbers
            2) Capital Letters
            3) Lowercase Leters
            4) Numbers + Capital Letters
            5) Numbers + Lowercase Leters
            6) Numbers + Capital Letters + Lowercase Leters
            7) Capital Letters + Lowercase Leters
            8) All Printable
            
            Choice:   ''')
        try:
            choice=int(choice)
        except:
            choice=0
except(KeyboardInterrupt):
    print "\n Received Ctrl+C, terminating...\n"
    sys.exit()

choice=int(choice)
poss=[]

if choice==1:
    poss=numb
elif choice==2:
    poss=cap
elif choice==3:
    poss=low
elif choice==4:
    poss=numb+cap
elif choice==5:
    poss=numb+low
elif choice==6:
    poss=numb+cap+low
elif choice==7:
    poss=cap+low
elif choice==8:
    poss=cap+low+numb+dig+other

bigList=[]
for i in poss:
    bigList.append(str(chr(i)))

hash=raw_input("\n MD5 HASH:  ")
if len(hash) != 32:
    print "\n THIS IS NOT AN MD5 HASH!!"
    raw_input("Press ENTER to exit...")
    sys.exit()

print ''
MIN=int(raw_input("Min length of the password: "))
MAX=int(raw_input("Max length of the password: "))
HOW_OFTEN_CHECK=50000
count=0
l=0
print "\n STARTING BRUTEFORCE OF HASH ",hash," ..."
START_TIME=time.time()

for i in range(MIN,MAX+1):
    for s in product(bigList,repeat=i):
        count+=1
        l+=1
        ha=hashlib.md5("".join(s)).hexdigest()
        if ha==hash:
            END_TIME=time.time()
            print "\r\n\r\n PASSWORD FOUND: ","".join(s),"\n"
            elapsed=END_TIME-START_TIME
            speed=int(l/elapsed)
            print speed,"combinations/sec"
            try:
                raw_input("Press ENTER to exit...")
                print ''
                sys.exit()
            except(KeyboardInterrupt):
                print "\nReceived Ctrl+C..."
                raw_input("Press ENTER to exit...")
                sys.exit()
        else:
            if "".join(s)=="z"*MAX:
                print "\r\n All possible",MAX,"symbols combinations checked, but password not found!"
                raw_input("Press ENTER to exit...")
                sys.exit()
        if count>=HOW_OFTEN_CHECK:
            count=0
            res="{:,}".format(l)+" words generated. Current: "+"".join(s)
            update(res)