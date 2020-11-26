from robot import Robot

def test_robot_equivalence():
    rob1 = Robot("rob")
    rob2 = Robot("rob")
    assert rob1 == rob2

def test_robot_different_name():
    rob = Robot("rob")
    bob = Robot("bob")
    assert rob != bob
    