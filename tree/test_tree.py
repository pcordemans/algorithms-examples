from tree import Tree

def test_empty_tree():
    t = Tree()
    assert t.size() == 1
    assert t.ls() == []

def test_touch():
    t = Tree()
    t.touch("filename", 3)
    assert t.size() == 4
    assert t.ls() == ["f: filename"]
    t.touch("anotherfile", 42)
    assert t.size() == 46
    assert t.ls() == ["f: filename", "f: anotherfile"]

def test_mkdir():
    t = Tree()
    t.mkdir("directory")
    assert t.size() == 2
    assert t.ls() == ["d: directory"]
    t.mkdir("anotherdirectory")
    assert t.size() == 3
    assert t.ls() == ["d: directory", "d: anotherdirectory"]
