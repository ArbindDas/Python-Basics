def switch_case(value):
    return {
        1: "One",
        2: "Two",
        3: "Three"
    }.get(value, "Invalid")

print(switch_case(1))
print(switch_case(4))