x = 75
if x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70:
    print("Grade: C")
elif x >= 60:
    print("Grade: D")
else:
    print("Grade: F")

x = 10
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is not a positive number")

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)