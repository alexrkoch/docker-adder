first_input = input('Please enter an integer:\n')
second_input = input('Please enter a second integer to add to the first:\n')
def add_function(a, b):
  a = int(first_input)
  b = int(second_input)
  return a + b
result = add_function(first_input, second_input)
print(f"Your two numbers added together equal {result}")