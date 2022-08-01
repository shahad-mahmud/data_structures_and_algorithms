def is_balanced(string):
    stack = []

    for paran in string:
        if paran in ['(', '{', '[']:
            stack.append(paran)
            continue
        if not stack:
            return False
        current_paran = stack.pop()

        if paran == ')' and current_paran != '(':
            return False
        if paran == '}' and current_paran != '{':
            return False
        if paran == ']' and current_paran != '[':
            return False
    return not stack

print(is_balanced('[{(]})'))
