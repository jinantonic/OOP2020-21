#A separate class for Product
class Product:
  
    # Constructor function wth price and discount
    def __init__(self, price, disc_stra = None):
          
        # take price and discount strategy
        self.price = price
        self.disc_stra = disc_stra
          
    # A separate function for price after discount
    def price_after_disc(self):
        if self.disc_stra:
            disc = self.disc_stra(self)
        else:
            disc = 0
              
        return self.price - disc
  
    def __repr__(self):
          
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_disc())
  
# Function dedicated to On Sale Discount
def on_sale(order):
    return order.price * 0.25 + 20
  
# function dedicated to 20 % discount
def twenty_disc(order):
    return order.price * 0.20
  
# main function
if __name__ == "__main__":
    print(Product(10000))
      
    # With discount strategy of 20 % discount
    print(Product(10000, disc_stra = twenty_disc))
  
    # With discount strategy of On Sale discount
    print(Product(10000, disc_stra = on_sale))