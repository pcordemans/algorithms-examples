from stack import Stack

def test_push_isEmpty():
    stack = Stack()
    assert stack.isEmpty()
    stack.push("1")
    assert not stack.isEmpty()

def test_push_top():
    stack = Stack()
    stack.push("1")
    assert stack.top() == "1"
    stack.push("2")
    assert stack.top() == "2"

def test_push_pop():
    stack = Stack()
    stack.push("1")
    assert stack.pop() == "1"
    assert stack.isEmpty()

def test_push_pop_multiple():
    stack = Stack()
    stack.push("1")
    stack.push("2")
    assert stack.pop() == "2"
    assert stack.pop() == "1"
    assert stack.isEmpty()