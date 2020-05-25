def read_age():
    age = int(input("Enter your age: "))
    if age < 0 or age > 110:
        raise ValueError("Invalid age")

    return age

try:
    val = read_age()
    print(f"Your age is {val}")

except ValueError as e:
    print(e)