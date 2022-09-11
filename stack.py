# create a stack

def create_stack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        return 'Stack is empty'

    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("Popped item: " + pop(stack))
print("Stack after popping an element: " + str(stack))
