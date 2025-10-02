import math

class Calculator:
    def add(self, a, b):
        """ Adds two numbers """
        return a + b
    def subtract(self, a, b):
        """ Subtracts two numbers """
        return a - b
    def multiply(self, a, b):
        """ Multiplies two numbers """
        return a * b
    def divide(self, a, b):
        """ Divides two numbers """
        return a / b
    def exponentiate(self, a, b):
        """ Raises a number to the power of another number """
        return a ** b

    def get_sum(self, numbers):
        """ Adds multiple numbers """
        return sum(numbers)

    def get_difference(self, numbers):
        """ Subtracts multiple numbers """
        return numbers[0] - self.get_sum(numbers[1:])

    def get_product(self, numbers):
        """ Multiplies multiple numbers """
        return math.prod(numbers)

    def get_quotient(self, numbers):
        """ Divides multiple numbers """
        result = numbers[0]
        for n in numbers[1:]:
            result /= n
        return result

print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")

base_operation = "X two numbers"
base_multiple_operation = "X multiple numbers"
two_numbers_operations = [base_operation.replace("X", "add"), base_operation.replace("X", "subtract"), base_operation.replace("X", "multiply"), base_operation.replace("X", "divide"), base_operation.replace("X", "exponentiate")]
multiple_numbers_operations = [base_multiple_operation.replace("X", "add"), base_multiple_operation.replace("X", "subtract"), base_multiple_operation.replace("X", "multiply"), base_multiple_operation.replace("X", "divide")]
operations = [*two_numbers_operations,  *multiple_numbers_operations]

user_choice_prompt = "\n".join([f"({i+1}) {operation}" for i, operation in enumerate(operations)])
userChoice = input(user_choice_prompt + "\n")
multiple_numbers_choices = ["6", "7", "8", "9"]

firstNumber =  int(input("Type the first number:")) if userChoice not in multiple_numbers_choices else None
secondNumber = int(input("Type the second number:")) if userChoice not in multiple_numbers_choices else None

numbers = []
base_numbers_prompt = "Type the numbers to X separated by spaces: "
if userChoice == "6":
    numbers = input(base_numbers_prompt.replace("X", "add"))
elif userChoice == "7":
    numbers = input(base_numbers_prompt.replace("X", "subtract"))
elif userChoice == "8":
    numbers = input(base_numbers_prompt.replace("X", "multiply"))
elif userChoice == "9":
    numbers = input(base_numbers_prompt.replace("X", "divide"))

numbers = [int(number) for number in numbers.split()]
log = "The A of B and C is D"
calculator = Calculator()

match userChoice:
    case "1":
        result = calculator.add(firstNumber, secondNumber)
        log = log.replace("A", "sum").replace("B", str(firstNumber)).replace("C", str(secondNumber)).replace("D", str(result))
    case "2":
        result = calculator.subtract(firstNumber, secondNumber)
        log = log.replace("A", "difference").replace("B", str(firstNumber)).replace("C", str(secondNumber)).replace("D", str(result))
    case "3":
        result = calculator.multiply(firstNumber, secondNumber)
        log = log.replace("A", "product").replace("B", str(firstNumber)).replace("C", str(secondNumber)).replace("D", str(result))
    case "4":
        result = calculator.divide(firstNumber, secondNumber)
        log = log.replace("A", "quotient").replace("B", str(firstNumber)).replace("C", str(secondNumber)).replace("D", str(result))
    case "5":
        result = calculator.exponentiate(firstNumber, secondNumber)
        log = log.replace("A", "exponentiation").replace("B", str(firstNumber)).replace("C", str(secondNumber)).replace("D", str(result))
    case "6":
        result = calculator.get_sum(numbers)
        numbers_str = " + ".join(str(number) for number in numbers)
        log = log.replace("A", "sum").replace("B", numbers_str).replace(" and C", "").replace("D", str(result))
    case "7":
        result = calculator.get_difference(numbers)
        numbers_str = " - ".join(str(number) for number in numbers)
        log = log.replace("A", "difference").replace("B", numbers_str).replace(" and C", "").replace("D", str(result))
    case "8":
        result = calculator.get_product(numbers)
        numbers_str = " * ".join(str(number) for number in numbers)
        log = log.replace("A", "product").replace("B", numbers_str).replace(" and C", "").replace("D", str(result))
    case "9":
        result = calculator.get_quotient(numbers)
        numbers_str = " / ".join(str(number) for number in numbers)
        log = log.replace("A", "quotient").replace("B", numbers_str).replace(" and C", "").replace("D", str(result))
    case _:
        log = "Invalid menu choice."

print(log)