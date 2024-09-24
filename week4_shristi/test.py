import example_pybind

# Test the greet function
print(example_pybind.greet("World"))

# Test the reverse_list function
numbers = [1, 2, 3, 4, 5]
reversed_numbers = example_pybind.reverse_list(numbers)
print(f"Original list: {numbers}")
print(f"Reversed list: {reversed_numbers}")
