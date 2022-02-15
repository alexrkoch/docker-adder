import pytest
import adder

def test_adder1():
  set_keyboard_input(["3", "4"])
  assert adder.add_function(3, 4) == 7

def test_adder2():
  set_keyboard_input(["39", "6"])
  assert adder.add_function(39, 6) == 45