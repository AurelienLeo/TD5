class Book:
    def __init__(self,name):
        self.name=name
        self.list_buy = list()
        self.list_sell = list()
        self.count_order=0

    def insert_buy(self,qtty,price):
        self.count_order += 1
        self.list_buy.append(Order(True,qtty,price,self.count_order))
        self.list_buy=sorted(sorted(self.list_buy, key=lambda x:x.id),key=lambda x:x.price, reverse = True)
        for i in self.list_sell:
            print(i)
        for i in self.list_buy:
            print(i)
        print("----------------------")

   
            
    def insert_sell(self,qtty,price):
        self.count_order += 1
        temp_qtty = qtty
        possible = False
        for i in self.list_buy:
            if price >= i.price:
                if temp_qtty >= i.qtty:
                    temp_qtty - i.qtty
                else:
                    possible = True
                    break
        if possible:
            for i in self.list_buy:
                if price>=i.price:
                    if temp_qtty > i.qtty:
                        temp_qtty-i.qtty
                        print("Execute " + str(qtty-temp_qtty) + " at " + str(i.price) + " on " + self.name)
                        self.list_buy.pop(i)
                    else:
                        i.qtty -= temp_qtty
                        print("Execute " + str(temp_qtty)+" at "+str(price)+" on "+self.name)
                        break
        if not possible:
            self.list_sell.append(Order(False,qtty,price,self.count_order))
        self.list_sell=sorted(sorted(self.list_sell, key=lambda x:x.id),key=lambda x:x.price, reverse = True)
        for i in self.list_sell:
            print(i)
        for i in self.list_buy:
            print(i)
        print("----------------------")




class Order:
    def __init__(self,buy,qtty,price,id):
        self.buy=buy
        self.qtty=qtty
        self.price=price
<<<<<<< HEAD
        self.id=id 
=======
        self.id=id
    
    def isBuy(self):
        msg = "SELL"
        if self.buy:
            msg = "BUY"
        return msg
>>>>>>> 5e121d6106af18ac2c6a54d1a81ab3ce53862c8b

    def __str__(self):
       type = self.isBuy()
       msg = type + " " + str(self.qtty) +"@"+ str(self.price) + " id=" + str(self.id)
       return msg

