class Book:
    def __init__(self,name):
        self.name=name
        self.list = list()

    def insert_buy(self,qtty,price):
        self.list.append(Order(true,qtty,price,len(self.list))
    
    def insert_sell(self,qtty,price):
        self.list.append(Order(false,qtty,price,len(self.list))


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

    def __str__


