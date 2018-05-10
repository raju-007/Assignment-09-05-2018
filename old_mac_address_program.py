li=[]
with open("mac.txt") as fo:
    zoo=fo.readlines()
    for rec in zoo:
        li+=rec.split()
    print("before sort")
    print(li)
    print("after sort")
    for i in range(0, len(li)):
        for j in range(0, len(li) - i - 1):
            if str(li[j]) > str(li[j + 1]):
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp

    print(li)
    f1=open("sam.txt","w+")
    j=[]
    for i in li:
        if len(i)== 17:
            if (i[0]>='1' or i[0]<='9' or i[0]>='a' or i[0]<='z' or i[0]>='A' or i[0]<='Z') and (i[1]>='1' or i[1]<='9' or i[1]>='a' or i[1]<='z' or i[1]>='A' or i[1]<='Z') and (i[3]>='1' or i[3]<='9' or i[3]>='a' or i[3]<='z' or i[3]>='A' or i[3]<='Z') and (i[4]>='1' or i[4]<='9' or i[4]>='a' or i[4]<='z' or i[4]>='A' or i[4]<='Z') and (i[6]>='1' or i[6]<='9' or i[6]>='a' or i[6]<='z' or i[6]>='A' or i[6]<='Z') and (i[7]>='1' or i[7]<='9' or i[7]>='a' or i[7]<='z' or i[7]>='A' or i[7]<='Z') and (i[9]>='1' or i[9]<='9' or i[9]>='a' or i[9]<='z' or i[9]>='A' or i[9]<='Z') and (i[10]>='1' or i[10]<='9' or i[10]>='a' or i[10]<='z' or i[10]>='A' or i[10]<='Z') and (i[12]>='1' or i[12]<='9' or i[12]>='a' or i[12]<='z' or i[12]>='A' or i[12]<='Z') and (i[13]>='1' or i[13]<='9' or i[13]>='a' or i[13]<='z' or i[13]>='A' or i[13]<='Z') and (i[15]>='1' or i[15]<='9' or i[15]>='a' or i[15]<='z' or i[15]>='A' or i[15]<='Z') and (i[16]>='1' or i[16]<='9' or i[16]>='a' or i[16]<='z' or i[16]>='A' or i[16]<='Z'):
                if i[2]=='-' and i[5]=='-' and i[8]=='-' and i[11]=='-' and i[14]=='-' :
                    j.append(i)

    print(j)
    f2=open("k1.txt","w+")
    count=0
    for h in j:
        f2.write("%s\n" % h)
        count+=1
    print ("total number of mac address present is= "+str(count))

