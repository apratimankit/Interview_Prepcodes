#Twosum
h=[1,4,45,6,10,8]
k=len(h)
g=set()
m=5
k1=[]
for i in range(len(h)):
    t=m-h[i]
    if t in g:
        print(str(h[i]),str(t))
    g.add(h[i])
#print(k1)
