def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Dictionary for operations
equation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  first_digit = int(input("Enter the first number: "))

  to_continue = 'yes'
  while to_continue == 'yes':
      choice = input('Please select the mathematical operator: "+", "-", "*", "/"\n')

      if choice in equation:
          next_digit = int(input("Enter the next number: "))
          operation_function = equation[choice]
          result = operation_function(first_digit, next_digit)
          print(f"The result of {first_digit} {choice} {next_digit} is {result}")

          # Ask if user wants to continue with the result
          to_continue = input(f"If you want to continue calculating with the result {result}, type 'yes'. Otherwise, type 'no' to start a new calculation: ").lower()

          if to_continue == 'yes':
              first_digit = result  # Update the first_digit to the result for the next operation
          else:
              to_continue = 'no'
      else:
          print("Invalid operator. Please try again.")

calculator()

