from src.math_operation import add , sub


def test_add():
    assert add(5,5)==10
    assert add(5,2)==7
    assert add(4,5)==9
    assert add(4,6)==11

def test_sub():
    assert sub(5 ,5 )==0
    assert sub (5,2)==3

    assert sub(6,6) == 0

