# test_* or test*

import pytest


def test_add(start1, start4):
    print(5+5)
    print("return statement", start1)# multiple retuen it is a tuple
    assert 5>2


def test_sub(start1, start4):
    print(5-2)
    assert 5 < 2


def test_mul(start1,start2, start4):
    print(3*4)
    assert True

def test_sqr(start2, start4):
    print(6*6)
    assert False, "test failed"