a=input("enter texts: ")
c=input("enter your searched word: ")
count=0
k=0
for i in a:
    d=a.split(' ')
if(d[k]=='.'):
    d.remove('.')
elif(d[k]==','):
    d.remove(',')
elif(d[k]==''):
    d.remove('')
else:
    while(k<len(d)):
        if(d[k]==c):
            count=count+1
        k=k+1
print('total number of words '+str(len(d)))
