#stack  and stack operations 
stack = []

#push
stack.append('A')
stack.append('B')
stack.append('C')
print("stack: ", stack)

#pop
element = stack.pop()
print("pop: ", element)

#peek
topElement = stack[-1]
print("peek: ", topElement)

#isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

#size
print("size: ",len(stack))

