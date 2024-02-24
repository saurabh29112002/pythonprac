# Problem age categrozitation

age = int(input("Enter Age: "))

if age <= 13:
    print("He / She is a child")
elif age > 13 and age < 19:
    print("He / She is a teenager")
elif age >= 19 and age < 59:
    print("He / She is a adult")
else:
    print("He / She is a senior citizen")