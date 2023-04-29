import sys

try:
    hrs_worked = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    sys.exit()

threshold_hrs = 40
pay_multiple = 1.5
if hrs_worked > threshold_hrs:
    pay = rate * (threshold_hrs + pay_multiple * (hrs_worked - threshold_hrs))
else:
    pay = rate * hrs_worked

print("Pay:", round(pay, 2))
