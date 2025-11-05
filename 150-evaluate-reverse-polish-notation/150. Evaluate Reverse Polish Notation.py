class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid = {"+", "-", "*", "/"}
        for num in tokens:
            if num not in valid:
                stack.append(int(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if num == "+":
                    stack.append(num1+num2)
                elif num == "-":
                    stack.append(num2-num1)
                elif num == "*":
                    stack.append(num1*num2)
                elif num == "/":
                    stack.append(int(num2/num1))
        return stack[0]