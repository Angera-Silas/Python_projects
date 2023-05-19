def birthYear(age):
    return (lambda a,b:(a-age)+b)(47,1975)
age=int(input("Enter your age : "))
print(f"The year you were born is : {age}")