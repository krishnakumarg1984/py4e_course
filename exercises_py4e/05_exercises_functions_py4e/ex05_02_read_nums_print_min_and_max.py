num_str = None
smallest = None
largest = None
while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        num = int(num_str)
    except:
        print("Invalid input")
        continue
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)
