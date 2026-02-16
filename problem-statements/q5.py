def calculate(expression: str) -> float:
    s = expression.replace(" ", "")
    stack = []
    i = 0
    sign = "+"
    
    while i < len(s):
        if s[i] in "+-*/" and not (s[i] == '-' and (i == 0 or s[i-1] in "+-*/")):
            sign = s[i]
            i += 1
            continue
            
        start = i
        if s[i] == '-':
            i += 1
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
            
        num = float(s[start:i])
        
        if sign == "+":
            stack.append(num)
        elif sign == "-":
            stack.append(-num)
        elif sign == "*":
            stack[-1] *= num
        elif sign == "/":
            stack[-1] /= num
            
    return round(sum(stack), 2)
