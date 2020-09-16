m = float(input("input the mass in grams:"))
T = float(input("input the change of temperature:"))
q = 4186*m*T
price = q*8.9 /2.7 * 10**(-7)
price = round(q, 2)
print(q)
print("price:", price, " cents:")