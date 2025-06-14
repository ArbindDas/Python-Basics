a = 5
b = 2

# Arithmetic operator: addition
print("a + b =", a + b)  
# Output: 7
# Adds the values of a and b

# Comparison operator: greater than
print("a > b is", a > b)  
# Output: True
# Checks if a is greater than b

# Logical operator: and
print("a and b is", a and b)  
# Output: 2
# 'and' returns the first falsy value or last value if all are truthy
# Here, both a and b are non-zero (truthy), so returns b (2)

# Bitwise OR operator: |
print("a | b is", a | b)  
# Output: 7
# Bitwise OR between binary of 5 (0101) and 2 (0010) is 0111 (decimal 7)

# Identity operator: is
print("a is b:", a is b)  
# Output: False
# Checks whether a and b reference the exact same object (memory location)

# Membership operator: in
print("a in [1, 2, 3, 5]:", a in [1, 2, 3, 5])  
# Output: True
# Checks whether the value of a exists inside the list
