#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

assert run("2 / -1").exit_status != 0
assert run("2 @ -1").exit_status != 0



###

print("All tests passed!")