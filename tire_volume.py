# As creativity, I added to the code the ability to ask whether the customer wants to buy the tire or not,
# with this, I opened an IF and ELSE system, as well as allowing the code to store the contact number
# and send it to VOLUMES.TXT. 

import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

calculation_one = width * aspect_ratio + 2540 * diameter

calculation_two = math.pi * width ** 2 * aspect_ratio
volume= (calculation_one * calculation_two) / 10000000000
print(f"The approximate volume is {volume:.2f} liters ")

from datetime import datetime
current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:

    print(file=volumes_file)
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file )

finish = input("Do you want to buy this kind of tire? (YES/NO): ")
if finish.lower() == "yes":
    number = input("Save your phone number here: ")
    with open("volumes.txt", "at") as volumes_file:
        print(f"Phone number: {number}" , file=volumes_file)
    print("Thanks for your time, we'll get back to you")

else:
    print("Thank you for your time. God bye!")
