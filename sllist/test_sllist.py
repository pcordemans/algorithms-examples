from sllist import SingleLinkedList

def test_prepend_list():
    list = SingleLinkedList()
    assert list.head() is None
    list.prepend(1).prepend(2).prepend(3)
    assert list.head() == 3

def test_tail_list():
    list = SingleLinkedList()
    list.prepend(1).prepend(2).prepend(3)
    assert list.tail().head() == 2
    assert list.tail().tail().head() == 1

def test_tail_empty_list():
    list = SingleLinkedList()
    assert list.tail().isEmpty()

def test_size():
    list = SingleLinkedList()
    assert list.size() == 0
    list.prepend(1).prepend(2).prepend(3)
    assert list.size() == 3