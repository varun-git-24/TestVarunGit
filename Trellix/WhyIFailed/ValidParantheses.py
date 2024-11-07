



def valid_parantheses(characters):
    list_stack = []
    for character in characters:
        if character == '{' and character not in list_stack:
            list_stack.append('{')
        if character == '[' and character not in list_stack:
            list_stack.append('[')
        if character == '(' and character not in list_stack:
            list_stack.append('(')
        if character == ")" and list_stack[len(list_stack)-1] == '(':
            list_stack.pop()
        if character == "]" and list_stack[len(list_stack) - 1] == '[':
            list_stack.pop()
        if character == "}" and list_stack[len(list_stack) - 1] == '{':
            list_stack.pop()


    return len(list_stack)

x = '{[]}([{}]){}()'
y = '{(})'

valid = valid_parantheses(x)
if valid == 0:
    print('Valid Parantheses')
else:
    print('Invalid Parantheses')










