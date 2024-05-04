import math


items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))
answer = math.ceil(items/items_per_box)
print(f"For {items} items, packing {items_per_box} items in each box, you will need {answer} boxes.")
