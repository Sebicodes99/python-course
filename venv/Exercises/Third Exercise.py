weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit == "K" or "k":
    result = int(weight) / 0.45359237
    print("Your weight in Lbs is: " + str(result))
elif unit == "L" or "l":
    result = int(weight) * 0.45359237
    print("Your Weight in Kgs is: " + str(result))
else:
    print("Check the writing!")
    
