class StackEmptyError(Exception):
    def __str__(self):
        return "Stack is empty"


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.length == 0:
            raise StackEmptyError()

        return self.data.pop()

    @property
    def length(self):
        return len(self.data)


s = Stack()
try:
    print(s.pop())
except ValueError as ex:
    print(ex)

s.push(100)
s.push(200)
print(s.pop())
print(s.length)
