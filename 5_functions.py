def add(x, y):
    return x + y

def greet(name="User"):
    return "Hello " + name

print(add(2, 3))
print(greet())




def greet_user(name, hour):
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"

print(greet_user("Arbind", 14))




def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))



def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("Temp in °F:", celsius_to_fahrenheit(25))
