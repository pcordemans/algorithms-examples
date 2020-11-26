from dllist import DoubleLinkedList

def test_empty_list():
    list = DoubleLinkedList()
    assert list.isEmpty()


def test_add_no_longer_empty():
    list = DoubleLinkedList()
    list.addFront("element")
    assert not list.isEmpty()


def test_add_front_one_element():
    list = DoubleLinkedList()
    list.addFront("element")
    assert list.front() == "element"
    assert list.back() == "element"


def test_add_back_one_element():
    list = DoubleLinkedList()
    list.addBack("element")
    assert list.front() == "element"
    assert list.back() == "element"

def test_add_multiple_elements():
    list = DoubleLinkedList()
    list.addFront("first")
    list.addBack("second")
    assert list.front() == "first"
    assert list.back() == "second"
    list.addFront("beforefirst")
    assert list.front() == "beforefirst"
    assert list.back() == "second"
    list.addBack("behindsecond")
    assert list.front() == "beforefirst"
    assert list.back() == "behindsecond"

def test_remove_front():
    list = DoubleLinkedList()
    list.addFront("first")
    list.addBack("second")
    assert list.removeFront() == "first"
    assert list.front() == "second"
    assert list.removeFront() == "second"
    assert list.front() is None
