def zeronotrequired(func):
    def wrapper(n1,n2):
        if (n1==0) | (n2==0):
            raise Exception('invalid  parameter')
        else:
            return func(n1,n2)
    return wrapper

def newdiv(func):
    def wrapper(n1,n2):
        if n1>n2:
            return func(n1,n2)
        else:
            return func(n2,n1)
    return wrapper

# @newdiv
@zeronotrequired
def div(n1,n2):
    return n1/n2

try:
    print(div(5,0))

except Exception as e:
    print(e.args)