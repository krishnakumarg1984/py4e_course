numlist = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
        numlist.append(num)
    except:
        print("Invalid input. Try again or enter 'done' to quit")
        continue

print(f"Maximum: {max(numlist)}")
print(f"Minimum: {min(numlist)}")
