l=[1,2,3,4,5,6,7,8,9]
sq=list(map(lambda num:num**2,l))
print(sq)

products=[
    {'name':'boost','mrp':100,'stock':200},
    {'name':'horlicks','mrp':100,'stock':200},
    {'name':'viva','mrp':100,'stock':200},
    {'name':'complan','mrp':100,'stock':200}
    ]
print(products)
for i in products:
    print(i)
    print(i['name'])

listname=list(map(lambda n:n['name'],products))
print(listname)