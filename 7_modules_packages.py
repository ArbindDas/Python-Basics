
import math

# Square root
print("√25:", math.sqrt(25))

# Power
print("2^3:", math.pow(2, 3))

# Trigonometric
print("sin(90°):", math.sin(math.radians(90)))

# Constants
print("π (pi):", math.pi)
print("e (Euler's number):", math.e)

# Logarithm
print("log10(1000):", math.log10(1000))

# Ceiling and Floor
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))


# datetime Module Examples
import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Custom date
d = datetime.datetime(2023, 12, 25)
print("Christmas:", d)

# Format date
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Difference between dates
date1 = datetime.datetime(2024, 1, 1)
date2 = datetime.datetime(2025, 1, 1)
diff = date2 - date1
print("Days between:", diff.days)

# Add days to date
future = now + datetime.timedelta(days=30)
print("30 days from now:", future)






