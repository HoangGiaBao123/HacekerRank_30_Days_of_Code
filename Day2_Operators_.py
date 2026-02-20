import math
import os
import random
import re
import sys

def total_bill(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost / 100) * tip_percent
    tax = meal_cost * (tax_percent / 100)
    total = meal_cost + tip + tax
    
    return round(total)

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    print(total_bill(meal_cost, tip_percent, tax_percent))
