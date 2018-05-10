k=int(input("enter the size of list "))
z=1
a=[]
sum1=0
for i in range(k):
    i = int(input("enter list " + str(z) + " value\n"))
    a.insert(k, int(i))
    z = z + 1
print(a)
for i in a:
    sum1+=i
print("sum of a list is= "+str(sum1))
print("#################################")
su = [a[0]]
# su.append(a[0])
for i in range(1, len(a)):
    su.append(abs(a[i]-a[i-1]))
print(su)
sum2=0
for j in su:
    sum2+=j
print("sum of list 2 is "+str(sum2))
p=abs(sum1-sum2)
print("difference of two number is= "+str(p))