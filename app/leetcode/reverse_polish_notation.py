from typing import List


class Solution(object):
    # time complexity of O(n), where n is the number of tokens.
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand2 + operand1)
                elif token == '-':
                    stack.append(operand2 - operand1)
                elif token == '*':
                    stack.append(operand2 * operand1)
                elif token == '/':
                    stack.append(int(operand2 * 1.0 / operand1))

        return stack[-1]

###############################

#  Implementing a stack is a good idea for evaluating Reverse Polish Notation (RPN) because:
#
# 1. Natural Fit: RPN operations naturally lend themselves to a stack-based approach,
# as each operator typically acts on the operands immediately preceding it in the expression.
#
# 2. Efficient Parsing: Using a stack allows for efficient parsing of RPN expressions. As operands are encountered, they can be pushed onto the stack.
# When an operator is encountered, the necessary operands can be popped from the stack, and the result can be pushed back onto the stack.
#
# 3. Simple and Intuitive: The stack mimics the way RPN expressions are evaluated manually, making the implementation straightforward and intuitive.
# It simplifies the process of tracking operands and operators during evaluation.

###############################

# 150. Evaluate Reverse Polish Notation
# https://en.wikipedia.org/wiki/Reverse_Polish_notation

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# Constraints:
#
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


if __name__ == "__main__":

    sol = Solution()
    test1 = ["2", "1", "+", "3", "*"]
    test2 = ["4", "13", "5", "/", "+"]
    test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(sol.evalRPN(test3))

