import pandas as pd
class Book:
    def __init__(self,name):
        self.name=name
        self.list_buy = list()
        self.list_sell = list()
        self.count_order=0
        self.dfBuy = pd.DataFrame(columns=["Type","Quantity","Price"])
        self.dfSell = pd.DataFrame(columns=["Type","Quantity","Price"])

    def insert_buy(self,qtty,price):
        self.count_order += 1
        self.list_buy.append(Order(True,qtty,price,self.count_order))
        self.list_buy=sorted(sorted(self.list_buy, key=lambda x:x.id),key=lambda x:x.price, reverse = True)
        print(f"--- Insert BUY {qtty}@{price} id={self.count_order} on {self.name}")
        print(f"Book on {self.name}")
        self.dfBuy.loc[self.count_order] = ["BUY" , qtty, price]
        #self.dfBuy.append(["BUY",qtty,price,self.count_order])
        if len(self.dfSell) > 0:
            print(self.dfSell)
        print(self.dfBuy)
        """
        for i in self.list_sell:
            print(i)
        for i in self.list_buy:
            print(i)
        """
        print("--------------------------")

   
            
    def insert_sell(self,qtty,price):
        self.count_order += 1
        temp_qtty = qtty
        print(f"--- Insert SELL {qtty}@{price} id={self.count_order} on {self.name}")
        print(f"Book on {self.name}")
        possible = False
        for i in self.list_buy:
            if price <= i.price:
                if temp_qtty > i.qtty:
                    temp_qtty -= i.qtty
                else:
                    possible = True
                    break
        if possible:
            temp_qtty = qtty
            for i in self.list_buy:
                if price<=i.price:
                    self.list_buy = sorted(sorted(self.list_buy, key=lambda x: x.id), key=lambda x: x.price,
                                               reverse=True)
                    if temp_qtty > i.qtty:
                        temp_qtty-=i.qtty
                        print("Execute " + str(i.qtty) + " at " + str(i.price) + " on " + self.name)
                        self.dfBuy.drop(i.id, inplace=True)
                        self.list_buy.pop(self.list_buy.index(i))
                    else:
                        i.qtty -= temp_qtty
                        print("Execute " + str(temp_qtty)+" at "+str(i.price)+" on "+self.name)
                        self.dfBuy.loc[i.id] = ["BUY", i.qtty, i.price]
                        break
        if not possible:
            self.list_sell.append(Order(False,qtty,price,self.count_order))
            self.dfSell.loc[self.count_order] = ["SELL", qtty, price]
        self.list_sell=sorted(sorted(self.list_sell, key=lambda x:x.id),key=lambda x:x.price, reverse = True)
        """
        for i in self.list_sell:
            print(i)
        for i in self.list_buy:
            print(i)
        """
        print(self.dfSell)
        print(self.dfBuy)
        print("--------------------------")




class Order:
    def __init__(self,buy,qtty,price,id):
        self.buy=buy
        self.qtty=qtty
        self.price=price
        self.id=id
    
    def isBuy(self):
        msg = "SELL"
        if self.buy:
            msg = "BUY"
        return msg

    def __str__(self):
       type = self.isBuy()
       msg = type + " " + str(self.qtty) +"@"+ str(self.price) + " id=" + str(self.id)
       return msg
