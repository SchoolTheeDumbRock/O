ADD = '+'
MINUS = '-'
MUL = '*'
DIVIDE = '/'
NUM = int
OP = [ADD, MINUS, MUL, DIVIDE]

# Look up how to use the .split to make tokens

o = input("O:") #input

tokens = o.split(" ") #tokenize process and process info to determine stuff like operation

ostack = []                   #the stack
stack = ostack.append(tokens) #the stack

print(tokens)
print(ostack)
