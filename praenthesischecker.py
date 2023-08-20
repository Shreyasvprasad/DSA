def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False

            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False

    return not stack  # Return True if the stack is empty, False otherwise

# Driver code
exp1 = "[()]{}{[()()]()}"
exp2 = "[(])"

if is_balanced(exp1):
    print("balanced")
else:
    print("not balanced")

if is_balanced(exp2):
    print("balanced")
else:
    print("not balanced")
