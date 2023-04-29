import sys


def computepay(hours, rate):
    overtime_hrs = 40
    pay_factor = 1.5

    if hours > overtime_hrs:
        pay = rate * (overtime_hrs + pay_factor * (hours - overtime_hrs))
    else:
        pay = rate * hours

    return pay


try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    sys.exit()


print("Pay", round(computepay(hours, rate), 2))
