a = int(input("How many botles 1 liter or less? "))
b = int(input("How many botles more than 1 liter?"))
deposite = 0.1*a + 0.25*b
deposite = round(deposite, 2)
print(deposite,"$")