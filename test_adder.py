import pytest
from adder import add


def test_adder1():
  assert add(3, 4) == 7

def test_adder2():
  assert add(39, 6) == 45