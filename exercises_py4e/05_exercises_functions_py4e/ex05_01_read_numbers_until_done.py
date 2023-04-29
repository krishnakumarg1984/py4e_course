num_str = None
count = 0
total = 0.0
while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        num = float(num_str)
        count += 1
        total += num
    except:
        print("Invalid input")
        continue

print(total, count, total / count)
