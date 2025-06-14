x = 10
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal to 5")
else:
    print("Smaller or equal")

# For loop printing numbers and their squares
for i in range(5):
    print(f"Number: {i}, Square: {i**2}")

# For loop iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# While loop counting down from 5 to 1
i = 5
while i > 0:
    print("Countdown:", i)
    i -= 1

# While loop with break
i = 0
while True:
    if i == 3:
        print("Breaking loop")
        break
    print("i is:", i)
    i += 1
