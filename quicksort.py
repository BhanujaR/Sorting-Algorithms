from insertionsort import *
from mergesort import *


def quick_sort(Arr,l,h):
    if l<h:
        part1=partition(Arr,l,h)
        quick_sort(Arr,l,part1-1)
        quick_sort(Arr,part1+1,h)

def partition(Arr,l,h):
    pi=Arr[h]
    i=l-1
    for j in range(l,h):
        if Arr[j]<=pi:
            i=i+1
            (Arr[i],Arr[j])=(Arr[j],Arr[i])

    (Arr[i+1],Arr[h])=(Arr[h],Arr[i+1])
    return i+1

#calling quick sort for each list and calculating the execution time for the same
st_20=time.time()
quick_sort(sl2_20,0,len(sl2_20)-1)
Execution_time_20=time.time()-st_20

st_100=time.time()
quick_sort(sl2_100,0,len(sl2_100)-1)
#print(sl1_100)
Execution_time_20=time.time()-st_100

st_1000=time.time()
quick_sort(sl2_1000,0,len(sl2_1000)-1)
#print(sl1_1000)
Execution_time_20=time.time()-st_1000

st_4000=time.time()
quick_sort(sl2_4000,0,len(sl2_4000)-1)
#print(sl1_4000)
Execution_time_20=time.time()-st_4000

#writing to an output file
file=open("arrQK_O_20.txt","w")
for i in sl1_20:
    s= " ".join(str(n) for n in d1_20[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_20)+' seconds')

file=open("arrQK_O_100.txt","w")
for i in sl1_100:
    s= " ".join(str(n) for n in d1_100[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_100)+' seconds')

file=open("arrQK_O_1000.txt","w")
for i in sl1_1000:
    s= " ".join(str(n) for n in d1_1000[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_1000)+' seconds')

file=open("arrQK_O_4000.txt","w")
for i in sl1_4000:
    s= " ".join(str(n) for n in d1_4000[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_4000)+' seconds')