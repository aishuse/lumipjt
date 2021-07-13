class Book:
    book_list={
        'alchemist':{'name':'alchemist','author':'paulo','price':300,'av_copies':20,'sold':563},
        'Vivekadeepini': {'name': 'Vivekadeepini', 'author': 'Shankaracharya', 'price': 250, 'av_copies': 120, 'sold': 32},
        'Devadas': {'name': 'Devadas', 'author': 'sarat', 'price': 100, 'av_copies': 80, 'sold': 0},
        'Dharmashastra': {'name': 'Dharmashastra', 'author': 'manu', 'price': 50, 'av_copies': 158, 'sold': 66},
        'Gora': {'name': 'Gora', 'author': 'tagore', 'price': 90, 'av_copies': 250, 'sold': 88},
        'Meghdoot': {'name': 'Meghdoot', 'author': 'kalidas', 'price': 200, 'av_copies': 57, 'sold': 30},
        'Panchtantra': {'name': 'Panchtantra', 'author': 'vishnu', 'price': 60, 'av_copies': 128, 'sold': 110},

    }

    def find_book(self,name):

        self.name=name

        if name in Book.book_list:
            copies = Book.book_list[name]['av_copies']
            if copies>0:
                print('available copies of',name,copies)
                sold = Book.book_list[name]['sold']
                print('Book sold:',sold)
                price=Book.book_list[name]['price']
                print('price is ',price)
            else:
                print('out of stock')
        else:
            print('book not available')
    #
    def book_sort(self):
        print('List of highest sold books:')
        sorted_keys = sorted(Book.book_list, key=lambda x: (Book.book_list[x]['sold']),reverse=True)
        print(sorted_keys)

        sorted_list = sorted(Book.book_list.items(), key=lambda x: (x[1]['sold']),reverse=True)
        print(sorted_list)
        for i in sorted_list:
            print(i)




b=Book()
x=input('enter book needed: ')
b.find_book(x)
b.book_sort()