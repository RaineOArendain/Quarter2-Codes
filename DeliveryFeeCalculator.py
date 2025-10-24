
def calculate_delivery_fee(x, y):
    total = x * y
    return total

distfee = int(input("Enter the distance in kilometers: "))
phpkm = int(input("Enter the rate per kilometer (PHP): ")) 

fee = calculate_delivery_fee(distfee, phpkm)
print("Total Delivery Fee: ₱", fee)