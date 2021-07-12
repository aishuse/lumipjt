# l=[1,2,3,4,5,6,7,8,9]
# sq=list(filter(lambda num:num%2==0,l))
# print(sq)
#

products=[
    {'name':'boost','mrp':100,'stock':200},
    {'name':'horlicks','mrp':100,'stock':700},
    {'name':'viva','mrp':100,'stock':500},
    {'name':'complan','mrp':100,'stock':20},
    {'name':'bournvita','mrp':100,'stock':0},
    {'name':'lactare','mrp':100,'stock':0}
    ]

#
# outofstock=list(filter(lambda n:n['stock']==0,products))
# print(outofstock)
#
# listname=list(filter(lambda n:n['name']=='viva',products))
# print(listname)
#
# listname=list(filter(lambda n:n['stock']>200,products))
# print(listname)


#
# below=list(filter(lambda n:n['stock']<250,products))
# print(below)

l=[2,3,4,8,10,7]

def greater(n):
    if n<5:
        return n-1
    else:
        return n+1


lst=list(map(greater,l ))
print(lst)

x=list(map(lambda n:n+1 if n>5 else n-1,l))
print(x)


n1=10
n2=20
res=n1 if n1>n2 else n2
print(res)


n=7
r='odd' if n%2!=0 else 'even'
print(r)