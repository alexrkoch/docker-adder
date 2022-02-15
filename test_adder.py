import pytest
import adder

def test_adder1():
  assert adder.add_function(3, 4) == 7

def test_adder2():
  assert adder.add_function(3.5, 6) == 9.5