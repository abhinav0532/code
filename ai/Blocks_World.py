from pickle import GLOBAL


GLOBAL
stack1 = ["A", "B"]
stack2 = []

def move():
    blockRemoved = stack1.pop()
    stack2.append(blockRemoved)


move()
print(stack1)
print(stack2)