def login_required(func):
    def wrapper(self,acc_no,*args,**kwargs):
        if(self.session['user']==acc_no):
            return func(self,acc_no,*args,**kwargs)
        else:
            print('u must login')
    return wrapper

class Bank:

    users_list={
        1000:{'ac num':1000,'pswd':'user1','balance':5000},
        1001:{'ac num':1001,'pswd':'user2','balance':4000},
        1002:{'ac num':1002,'pswd':'user3','balance':100},
        1003:{'ac num':1003,'pswd':'user4','balance':5045},
        1004:{'ac num':1004,'pswd':'user5','balance':7895}

        }
    session={}
    session['user']=0
    def validateacc(self,acc_no):
        if acc_no in Bank.users_list:
            return True
        else:
            return False

    def authenticate(self,**kwargs):
        acc_no=kwargs['acc_no']
        pswd=kwargs['pswd']
        user=self.validateacc(acc_no)
        if user:
            if (pswd==self.users_list[acc_no]['pswd']):
                self.session['user']=acc_no
                return acc_no
            else:
                return -1   #invalid password

        else:
            return 0    #invalid acc_no

    @login_required
    def balance_enquiry(self,acc_no):
        if (acc_no==self.session['user']):
            print(self.users_list[acc_no]['balance'])
        # else:
        #     print('you must login')


    def fund_transfer(self,user,to_acc,amt):
        if self.validateacc(to_acc):
            balance=self.users_list[user]['balance']
            if balance<amt:
                print("insufficient balance")
            else:
                self.users_list[user]['balance']-=amt
                self.users_list[to_acc]['balance']+=amt


    def logout(self):
        self.session['user']=0


obj=Bank()
user=obj.authenticate(acc_no=1002,pswd='user3')
obj.balance_enquiry(user)

obj1=Bank()
user=obj1.authenticate(acc_no=1000,pswd='user1')
if (user==-1)| (user==0):
    print('failed')
else:
    obj1.balance_enquiry(user)
obj1.fund_transfer(user,1002,500)
obj1.balance_enquiry(user)



obj=Bank()
user=obj.authenticate(acc_no=1002,pswd='user3')
obj.balance_enquiry(user)