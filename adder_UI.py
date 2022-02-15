from adder import add

first_input = int(input('Please enter an integer:\n'))

second_input = int(input('Please enter a second integer to add to the first:\n'))

result = add(first_input, second_input)

print(f"Your two numbers added together equal {result}")