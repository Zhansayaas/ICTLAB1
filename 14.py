feet = int(input("Feet: "))
inch = int(input("Inches:"))
inch += feet * 12
cm = round(inch * 2.54, 1)
print("Your height is:", cm)