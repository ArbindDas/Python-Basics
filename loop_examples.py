class LoopExamples:
    
    def for_even_numbers(self):
        print("Even numbers from 1 to 10:")
        for i in range(1, 11):
            if i % 2 == 0:
                print(i)
        print()
    
    @staticmethod
    def for_sum_1_to_100():
        total = 0
        for i in range(1, 101):
            total += i
        print("Sum from 1 to 100:", total)
        print()
    
    def for_multiplication_table(self):
        print("Multiplication table of 5:")
        for i in range(1, 11):
            print(f"5 x {i} = {5 * i}")
        print()
    
    def for_loop_string_chars(self):
        word = "Python"
        print("Characters in 'Python':")
        for char in word:
            print(char)
        print()
    
    def while_countdown(self):
        print("Countdown from 5 to 1:")
        i = 5
        while i > 0:
            print(i)
            i -= 1
        print()
    
    def while_powers_of_two(self):
        print("Powers of 2 less than 100:")
        i = 1
        while i < 100:
            print(i)
            i *= 2
        print()
    
    def while_simulated_input(self):
        print("Simulated user input loop:")
        simulated_inputs = ["hello", "test", "exit"]
        index = 0
        while index < len(simulated_inputs):
            text = simulated_inputs[index]
            print("User typed:", text)
            if text.lower() == "exit":
                break
            index += 1
        print()
    
    def foreach_list_fruits(self):
        fruits = ["apple", "banana", "cherry"]
        print("List of fruits:")
        for fruit in fruits:
            print(fruit)
        print()
    
    def foreach_dict_items(self):
        person = {"name": "Arbind", "age": 21}
        print("Person dictionary items:")
        for key, value in person.items():
            print(f"{key}: {value}")
        print()

# Usage example:
loops = LoopExamples()
# loops.for_even_numbers()
LoopExamples.for_sum_1_to_100()

# loops.for_sum_1_to_100()
# loops.for_multiplication_table()
# Call any other methods similarly
