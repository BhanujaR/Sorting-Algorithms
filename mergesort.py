#imported list with sum of the random values from insertion sort

from insertionsort import *
import math
import sys,resource
sys.setrecursionlimit(10**7)

def merge_sort(A):
    if len(A)>1:
        q=math.floor(len(A)/2)
        L=A[0:q]
        R=A[q:len(A)]
        merge_sort(L)
        merge_sort(R)
        i=0
        j=0
        k=0
        while i<len(L)and j<len(R):
            if L[i]<=R[j]:
                A[k]=L[i]
                i=i+1
            else:
                A[k]=R[j]
                j=j+1
            k=k+1
        
        while i<len(L):
            A[k]=L[i]
            i=i+1
            k=k+1
        while j<len(R):
            A[k]=R[j]
            j=j+1
            k=k+1
        
#calling merge sort for each list and calculating the execution time for the same
st_20=time.time()          
merge_sort(sl1_20)
Execution_time_20=time.time()-st_20

st_100=time.time() 
merge_sort(sl1_100)
Execution_time_20=time.time()-st_100

st_1000=time.time() 
merge_sort(sl1_1000)
Execution_time_20=time.time()-st_1000

st_4000=time.time() 
merge_sort(sl1_4000)
Execution_time_20=time.time()-st_4000

#writing to an output file
file=open("arrMR_O_20.txt","w")
for i in sl1_20:
    s= " ".join(str(n) for n in d1_20[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_20)+' seconds')

file=open("arrMR_O_100.txt","w")
for i in sl1_100:
    s= " ".join(str(n) for n in d1_100[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_100)+' seconds')

file=open("arrMR_O_1000.txt","w")
for i in sl1_1000:
    s= " ".join(str(n) for n in d1_1000[i])
    file.write(s+" "+str(i)+"\n")
file.write(str(Execution_time_1000)+' seconds')

file=open("arrMR_O_4000.txt","w")
for i in sl1_4000:
    s= " ".join(str(n) for n in d1_4000[i])
    file.write(s+" "+str(i)+"\n")
