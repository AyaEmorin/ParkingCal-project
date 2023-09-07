nameplate = str(input("Input your nameplate : "))
hours = int(input("Input your hours : "))
cuschoice = str(input("Do you buy our goods?? Yes = Y No = N : "))

discounted = 20
discount = 0
billing = 0

if cuschoice == "Y" or cuschoice == "yes":
    billing = float(input("Input your billing Net total : "))
    if hours <= 3:
        discount = 0
        billing = discounted
    elif hours <= 24:
        discount = billing*0.05
        hourMinus = hours-3
        billing = discounted + (hourMinus*20) - discount
    else:
        discount = billing*0.05
        hourMinus = hours - 24
        billing = (discounted + (21*20) + (hourMinus*10)) - discount

elif cuschoice == "N" or cuschoice == "No":
    if hours <= 3:
        billing = 20
    elif hours <= 24:
        hourMinus = hours - 3
        billing = 20 + (hourMinus*20)
    else:
        hourMinus = hours - 24
        billing = discounted + (21*20) + (hourMinus*10)

print(f"\n------------billing------------")
print(f"NumPlate : {nameplate}\nDiscount : {discount} บาท\nDiscounted : {billing} บาท")
print("-"*31)
