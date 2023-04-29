# 3.1 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay the hourly rate for the hours up to 40 and
# 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours
# and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a
# number. Do not worry about error checking the user input - assume the user
# types numbers properly.

hrs_worked = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

threshold_hrs = 40
pay_multiple = 1.5
if hrs_worked > threshold_hrs:
    pay = rate * (threshold_hrs + pay_multiple * (hrs_worked - threshold_hrs))
else:
    pay = rate * hrs_worked

# print("Pay:", round(pay, 2))
print(round(pay, 2))
