class Book:
    def __init__(self,name):
        self.name=name
        self.list_buy = list()
        self.list_sell = list()
        self.count_order=0

    def insert_buy(self,qtty,price):
        self.count_order += 1
        self.list.append(Order(true,qtty,price,self.count_order))
        print(Order(true,qtty,price,self.count_order))
        self.list_buy=sorted(self.list_buy,key=lambda x:x.price)
        #self.list_buy=sorted(sorted(self.list_buy, key=lambda x:x.id),key=lambda x:x.price)

        for i in self.list_buy:
            print(i)
   
            
    def insert_sell(self,qtty,price):
        self.count_order += 1
        self.list_sell.append(Order(false,qtty,price,self.count_order))
        self.list_sell = sorted(sorted(self.list_sell, key=lambda x:x.id),key=lambda x:x.price)

class Order:
    def __init__(self,buy,qtty,price,id):
        self.buy=buy
        self.qtty=qtty
        self.price=price
        self.id=id
    
    def isBuy(self):
        msg = "Sell"
        if self.buy:
            msg = "Buy"
        return msg

    def __str__(self):
       type = self.isBuy
       msg = type + " " + str(self.qtty) +"@"+ str(self.price) + " id=" + str(self.id)
       return msg

