class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infix_to_postfix(self, expression):
        postfix = []
        stack = []
        
        for char in expression.split():
            if char.isdigit():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Discard '('
            else:
                while stack and stack[-1] != '(' and self.operators[char] <= self.operators.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ' '.join(postfix)

    def evaluate_postfix(self, postfix):
        stack = []

        for char in postfix.split():
            if char.isdigit():
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                elif char == '/':
                    stack.append(num1 / num2)
                elif char == '^':
                    stack.append(num1 ** num2)

        return stack.pop()

# Example usage:
calculator = Calculator()
infix_expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
postfix_expression = calculator.infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)

result = calculator.evaluate_postfix(postfix_expression)
print("Result:", result)
