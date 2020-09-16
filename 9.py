balance = float(input("BALANCE:"))
interest_price=0.04
year=int(input("YEAR:"))

for i in range(0,year):
    c = balance*interest_price 
    balance=c+balance    
print("%.2f"%balance)