def calculate_tax(Item,Price,Rate):
    return (0.01 *(Price*Rate)) + (Item + Price)
print (calculate_tax(200,10,3/8))

