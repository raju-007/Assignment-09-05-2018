print("enter the size of the list= ")
k=int(input())
a=[]
z=1
for i in range(k):
    k=int(input("enter list "+str(z)+" value\n"))
    a.insert(i,k)
    z=z+1
print(a)
print("#####################")
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(a)
