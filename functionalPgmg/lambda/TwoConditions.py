# l=[1,2,3,4,5,6,7,8,9,10]
#
# res=list(map(lambda n:n-1 if n<5 else n+1 if n>5 else n,l))
# print(res)


my_collection = {
   'KEY1':{'name':'foo','data':1351,'completed':100},
   'KEY2':{'name':'bar','data':1541,'completed':12},
   'KEY3':{'name':'baz','data':583,'completed':18}
}
sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['name']))
print(sorted_keys)
#
# def fun(i):
#
#     print(my_collection[i]['name'])
#
# for i in my_collection:
#
#     # print(i)
#     fun(i)
#
