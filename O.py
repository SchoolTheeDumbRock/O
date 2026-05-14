ADD = '+'
MINUS = '-'
MUL = '*'
DIVIDE = '/'
NUM = int
OP = [ADD, MINUS, MUL, DIVIDE]
#todo figure out llist seperation and generation so learn about that


# Look up how to use the .split to make tokens

o = input("O:") #input

tokens = o.split() #tokenize process and process info to determine stuff like operation

ostack = []                   #the stack
stack = ostack.append(tokens) #the stack

if ADD in tokens:
    print("it worked")
else:
    print("didn't ig")

# printing area 
print(tokens)
print(ostack)

