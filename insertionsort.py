# code to input random numbers into files
import random, time
from collections import defaultdict

file=open("arr20.txt","w")
numbers = list(range(1000))
i=0
sin=[]
while i<20:
    l=random.sample(numbers, 3)
    if sum(l) not in sin:
        s= " ".join(str(n) for n in l) 
        file.write(s+" "+str(sum(l))+"\n")
        i=i+1
        sin.append(sum(l))
        print()
file.close()

file1=open("arr100.txt","w")
numbers = list(range(1000))
i=0
sin1=[]
while i<100:
    l1=random.sample(numbers, 3)
    if sum(l1) not in sin1:
        s1= " ".join(str(n) for n in l1) 
        file1.write(s1+" "+str(sum(l1))+"\n")
        i=i+1
        sin1.append(sum(l1))
        print()
file1.close()

file2=open("arr1000.txt","w")
numbers = list(range(1000))
i=0
sin2=[]
while i<1000:
    l2=random.sample(numbers, 3)
    if sum(l2) not in sin2:
        s2= " ".join(str(n) for n in l2) 
        file2.write(s2+"\n")
        i=i+1
        sin2.append(sum(l2))
        print()
file2.close()

file3=open("arr4000.txt","w")
numbers = list(range(4000))
i=0
sin3=[]
while i<4000:
    l3=random.sample(numbers, 3)
    if sum(l3) not in sin3:
        s3= " ".join(str(n) for n in l3) 
        file3.write(s3+"\n")
        i=i+1
        sin3.append(sum(l3))
        print()
file3.close()

#reading text file to dictionary and inserting sum as a key for arr20
d1_20={}
for k in range(0,20):
    with open("arr20.txt") as f:
        firstline = f.readlines()[k].rstrip()
        l=[]
        for i in firstline.split():
            j=int(i)
            l.append(j)
    s=sum(l)
    d1_20[s]=l

#print(dict1_20)

sl_20=[]
sl1_20=[]
sl2_20=[]

for i in d1_20.keys():
        sl_20.append(i)
        sl1_20.append(i)
        sl2_20.append(i)

#reading text file to dictionary and inserting sum as a key for arr100
d1_100=defaultdict(list)
for k in range(0,100):
    with open("arr100.txt") as f:
        firstline = f.readlines()[k].rstrip()
        l=[]
        for i in firstline.split():
            j=int(i)
            l.append(j)
    s=sum(l)
    d1_100[s]=l

sl_100=[]
sl1_100=[]
sl2_100=[]
for i in d1_100.keys():
        sl_100.append(i)
        sl1_100.append(i)
        sl2_100.append(i)

#reading text file to dictionary and inserting sum as a key for arr1000
d1_1000={}
for k in range(0,1000):
    with open("arr1000.txt") as f:
        firstline = f.readlines()[k].rstrip()
        l=[]
        for i in firstline.split():
            j=int(i)
            l.append(j)
    s=sum(l)
    d1_1000[s]=l
#print(d1_100)
sl_1000=[]
sl1_1000=[]
sl2_1000=[]
for i in d1_1000.keys():
        sl_1000.append(i)
        sl1_1000.append(i)
        sl2_1000.append(i)

#reading text file to dictionary and inserting sum as a key for arr1000
d1_4000={}
for k in range(0,4000):
    with open("arr4000.txt") as f:
        firstline = f.readlines()[k].rstrip()
        l=[]
        for i in firstline.split():
            j=int(i)
            l.append(j)
    s=sum(l)
    d1_4000[s]=l
#print(d1_100)
sl_4000=[]
sl1_4000=[]
sl2_4000=[]
for i in d1_4000.keys():
        sl_4000.append(i)
        sl1_4000.append(i)
        sl2_4000.append(i)


#insertionSort

def i_s(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
                a[j + 1] = a[j]
                j=j-1
        a[j + 1] = key

#calling insertion sort for each list and calculating the execution time for the same
st_20=time.time()
i_s(sl_20)
Execution_time_20=time.time()-st_20


st_100=time.time()
i_s(sl_100)
Execution_time_100=time.time()-st_100

st_1000=time.time()
i_s(sl_1000)
Execution_time_1000=time.time()-st_1000

st_4000=time.time()
i_s(sl_4000)
Execution_time_4000=time.time()-st_4000

#writing to an output file
file=open("arrIS_O_20.txt","w")
for i in sl_20:
    s= " ".join(str(n) for n in d1_20[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_20)+' seconds')

file=open("arrIS_O_100.txt","w")
for i in sl_100:
        s= " ".join(str(n) for n in d1_100[i])
        file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_100)+' seconds')

file=open("arrIS_O_1000.txt","w")
for i in sl_1000:
    s= " ".join(str(n) for n in d1_1000[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_1000)+' seconds')

file=open("arrIS_O_4000.txt","w")
for i in sl_4000:
    s= " ".join(str(n) for n in d1_4000[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_4000)+' seconds')

   


