# List example
lst = [10, 20, 30, 40]
print(lst[-1])          # Last element
lst.append(50)
print(lst)

# Tuple example
tup = ("apple", "banana", "cherry")
print(tup[0])           # First element
print(len(tup))         # Length of tuple

# Set example
st = {"red", "green", "blue"}
st.add("yellow")
print("green" in st)    # Membership test
print(st)

# Dictionary example
dct = {"name": "Alice", "age": 25}
print(dct.get("name"))           # Safe access
print(dct.get("city", "N/A"))    # Default value if key not found
dct["age"] = 26
print(dct)

# Nested structures
nested_lst = [[1, 2], [3, 4]]
print(nested_lst[1][0])          # Access nested list

nested_dct = {"emp1": {"name": "Bob", "id": 101}, "emp2": {"name": "Eve", "id": 102}}
print(nested_dct["emp2"]["name"])

# Mixed types
mix = [1, (2, 3), {"a", "b"}, {"key": "value"}]
print(mix[1][1])                 # Tuple inside list
print("a" in mix[2])             # Set inside list
print(mix[3]["key"])             # Dictionary inside list
