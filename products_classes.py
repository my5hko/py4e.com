class ProductInStore(object):
    price = 9.99
    name = 'new product'
    qty_in_stock = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
	
    def set_price(self, price):
        self.price = price
        return self
			
    def set_name(self, name):
        self.name = name
        return self

    def set_stock(self, qty):
        self.qty_in_stock = qty
        return self
    
    def get_price(self):
        return self.price

    def report(self):
        return "%s of '%s' are left" % (self.qty_in_stock, self.name)
    
class SimpleProductInStore(ProductInStore):
    
    def get_price(self, option = None):
        return super(SimpleProductInStore, self).get_price()
    
    def report(self):
        return "-----\nsimple product report\n-----\n%s of '%s' are left \ncurrent price is %s" % (self.qty_in_stock, self.name, self.price)
    
class ConfigurableProductInStore(ProductInStore):
    option_prices = None
    option_stock = None

    def set_price(self, price, option = None):
#        price = super(ConfigurableProductInStore, self).set_price(price)

        if option != None and option in self.option_prices:
            self.option_prices[option] = price

        elif option != None and option not in self.option_prices :
            self.option_prices.update({option: price})

        else :   
            self.price = price
        return self   
    
    def get_price(self, option = None):
        price = super(ConfigurableProductInStore, self).get_price()

        if option != None and option in self.option_prices:
            price += self.option_prices[option]
        return price
    
    def set_stock(self, qty, option = None):
#        qty_in_stock = super(ConfigurableProductInStore, self).set_stock(qty)

        if option != None and option in self.option_stock:
            self.option_stock[option] = qty
        
        elif option != None and option not in self.option_stock:
            print("Do not forget to add price for", option)
            self.option_stock.update({option: qty})

        else :   
            self.qty_in_stock = qty

        if sum(self.option_stock.values()) >= self.qty_in_stock :
            self.qty_in_stock = sum(self.option_stock.values())
        else :
            print("Some product options are not added to stock")
        return self
    
    def get_stock(self) :
        return self.qty_in_stock
    
    def __init__(self, name, basic_price, add_prices):
        self.name = name
        self.price = basic_price
        self.option_prices = add_prices
        option_stock = {} # creating stock dict with values 0 for each option 
        for option in self.option_prices:
            option_stock.setdefault(option, 0)
            
        self.option_stock = option_stock
        

    def report(self):
        report = "-----\nconfigurable product report\n-----\n%s of '%s' are left \nbase price is %s" % (self.qty_in_stock, self.name, self.price)
        
        if len(self.option_prices):
            report += "\nproduct options:"
            for i in self.option_prices:
                report += "\n- %s : %s : qty: %s" % (i, self.option_prices[i], self.option_stock[i])
        return report
    

abn911 = ConfigurableProductInStore('Lego Mindstorm v1', 199.99, {'v1': 0, 'v1.1': 0, 'v2': 21.0, 'v3': 50.5})

abn911.set_price(222).set_name('Lego Mindstorm v2').set_stock(15)
#print(abn911.option_stock)

print(abn911.option_stock)
print(abn911.get_price())
print(abn911.option_prices)
abn911.set_stock(10, "v1")
print(abn911.get_stock())
abn911.set_stock(5, "v4").set_stock(11, 'v1.1')
print(abn911.option_stock)
print(abn911.get_stock())
abn911.set_price(25, "v4")
print(abn911.option_prices)
abn911.set_price(10.5, "v1")
print(abn911.option_prices)
print(abn911.get_price("v1"))
abn911.set_price(210)
print(abn911.get_price("v1"))

print(abn911.report())
#print('price for v3 is %s' % (abn911.get_price('v3')))
""" abn912 = SimpleProductInStore('Anakin action figure 921', 56.11)
abn912.set_stock(10)
print(abn912.report())
print('price is %s' % (abn912.get_price())) """