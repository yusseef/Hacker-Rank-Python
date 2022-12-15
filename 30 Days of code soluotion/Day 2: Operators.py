#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent*meal_cost) / 100
    tax = (tax_percent*meal_cost) / 100
    result = meal_cost + tip + tax
    print(f'{result:.0f}')

