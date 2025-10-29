age = int(input("Hi there! Please enter your age: "))

sum = 0

for y in range(1, age + 1):
    sum += y

print("The sum of all numbers from 1 to", age, "is: ", sum)