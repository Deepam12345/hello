def fun1(lis,d,an):
    u1=lis.pop(d+1)
    u2=lis.pop(d)
    u3=lis.pop(d-1)
    lis.insert(d-1,an)
    #print(lis)

def fun(lis):
    while(len(lis)!=1):
        if("**" in lis):
            d=lis.index("**")
            an=int(lis[d-1])**int(lis[d+1])         
            fun1(lis,d,an)
            
        elif("~" in lis):
            d=lis.index("~")
            an= ~int(lis[d+1])
            lis.remove(list[d+1])
            lis.remove(list[d])
            lis.insert(d,an)         
             
        elif("%" in lis):
            d=lis.index("%")
            an=int(lis[d-1])%int(lis[d+1])         
            fun1(lis,d,an)
        elif("/" in lis):
            d=lis.index("/")
            an=int(lis[d-1])//int(lis[d+1])         
            fun1(lis,d,an)
        
        
        elif("*" in lis ):
           d=lis.index("*")
           an=int(lis[d-1])*int(lis[d+1])
           fun1(lis,d,an)
        
        elif("+" in lis):
           d=lis.index("+")
           an=int(lis[d-1])+int(lis[d+1])
           fun1(lis,d,an)
   
        elif("-" in lis):
           d=lis.index("-")
           an=int(lis[d-1])-int(lis[d+1])
           fun1(lis,d,an)
        elif("<<" in lis):
            d=lis.index("<<")
            an=int(lis[d-1])<<int(lis[d+1])         
            fun1(lis,d,an)
        elif(">>" in lis):
            d=lis.index(">>")
            an=int(lis[d-1])>>int(lis[d+1])         
            fun1(lis,d,an) 
        elif("&" in lis):
            d=lis.index("&")
            an=int(lis[d-1])//int(lis[d+1])         
            fun1(lis,d,an)
        elif("^" in lis):
            d=lis.index("^")
            an=int(lis[d-1])^int(lis[d+1])         
            fun1(lis,d,an)
        else:#"|" in lis):
            d=lis.index("|")
            an=int(lis[d-1])|int(lis[d+1])         
            fun1(lis,d,an)
        #print(lis)    
    return(lis[0]) 
str=input("enter expression ")
for j in str:
    if j in "+*~-^<>/()":
      str=str.replace(j,"a"+j+"a")
i=0
while i<=len(str)-2:
    if str[i]=="a" and str[i+1]=="a":
        str=str.replace("aa","a")
    i=i+1
list= str.split("a")
#print(list)
if "*" in list or"<" in list or">" in list:
    s=0
    while s<=len(list)-2:
        if list[s]==list[s+1] and list[s]!=")":
            op=list[s]
            us=list.pop(s+1)
            uss=list.pop(s)
            list.insert(s,op+op)
        s=s+1
        
#print(list)    


while len(list)!=1:
    if "(" in list :
        if("" in list):
            list.remove("")
        #print(list)
        b=len(list)-list[::-1].index("(")-1
        
        bb=b; li=[ ]
        while list[b] != ")":
            li.append(list[b])
            
            u=list.pop(b)
            #print(list)
        li.remove(li[0])
          
        v=list.pop(b)
        #print(v)
        ans=fun(li)
        #print(ans)
        list.insert(b,ans)
        #list.insert(b,")")
        if len(list)==1:
          print(list[0])
    else:
        if "" in list:
          list.remove("")
        ans=fun(list)
        print(ans)    
#print(list[0])           
            
            
            