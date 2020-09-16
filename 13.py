
cents = int(input("Please enter a number of cents:")) 
toonies = int(cents / 200) 
cents -= toonies * 200
loonies = int(cents / 100) 
cents -= loonies * 100
quarters = int(cents/25)
cents -= quarters * 25
dimes = int(cents/10)
cents -= dimes * 10
nickels = int(cents/5) 
pennies = cents
print("The change using the smallest amount of change is...")
print("{} toonies, {} loonies, {} quarters, {} dimes, {} nickels, {} pennies".format(toonies, loonies, quarters, dimes, nickels, pennies))