# Calculator

def add(n1, n2):
  return(n1 + n2)
def subtract(n1, n2):
  return(n1 - n2)
def multiply(n1, n2):
  return(n1 * n2)
def divide(n1, n2):
  return(n1 / n2)

# create a dictionary to store the operations and their functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("Enter your first number : "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the above: ")
num2 = int(input("Enter your second number: "))

calc_function = operations[operation_symbol]
answer = calc_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
