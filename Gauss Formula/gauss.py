def get_number(comment):
    number = input(comment)
    if number.isdigit():
        return int(number)
    return get_number(comment)

print("Gauss Formula")

amount = get_number("Enter the amount of money you want to earn: ")
items = get_number("Enter number of days you want to spend (default=100): ")
min_max_sum = amount / items * 2
delta = min_max_sum / (items + 1)

print("Creating list...")

arr = list()
counter = delta
for i in range(items):
    arr.append(int(counter))
    counter += delta
arr_sum = sum(arr)

if amount > arr_sum:
    delta_plus = amount - arr_sum
    step = items / delta_plus
    for i in range(0, delta_plus):
        c = int(i * step)
        arr[c] += 1

print("List of payments")
counter = 1
for el in arr:
    print(str(counter) + " - " + str(el))
    counter += 1
input("Press enter to exit...")
