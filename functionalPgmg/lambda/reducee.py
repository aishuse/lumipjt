from functools import *
l=[1,2,3,4,5]
res=reduce(lambda a,b:a+b,l)
print(res)

large=reduce(lambda a,b:a if a>b else b,l)
print(large)

products=[
    {'name':'boost','mrp':100,'stock':200},
    {'name':'horlicks','mrp':108,'stock':700},
    {'name':'viva','mrp':700,'stock':500},
    {'name':'complan','mrp':140,'stock':20},
    {'name':'bournvita','mrp':150,'stock':0},
    {'name':'lactare','mrp':150,'stock':0}
    ]

price=list(map(lambda n:n['mrp'],products))
print(price)
high=reduce(lambda a,b:a if a>b else b,price)
print(high)
# or
price=max(list(map(lambda n:n['mrp'],products)))
print(price)


