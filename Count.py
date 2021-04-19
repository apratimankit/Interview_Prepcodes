#CountFrequency
from collections import Counter
A=[1,1,2,2,2,2,3]
x=int(input())
g=Counter(A)
m1=[]
for i,j in g.items():
    if i==x:
        m1.append(j)
print(m1)
        
        
