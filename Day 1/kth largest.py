#k largest
#Considering the array is unsorted
#brute approach
#sort the array,return the k-1 element
import heapq
li = [6, 7, 9, 4, 3, 5, 8, 10, 1]
k=int(input())
h=[]
d=[]
for i in li:
    heapq.heappush(h,i)
    if len(h)>k:
        heapq.heappop(h)
d.append(heapq.heappop(h))
print(d)
    
