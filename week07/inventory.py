# 1. The most suprising things was how you can state that an Error was caught without an error through python being shown. 
# 2. Instead of taking hours using excel to to format sales, inventory, etc from multiple sheets, lists can be used to format data much quicker.


# Exercise 1: Build a list

print("--- Exercise 1: Build a list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # Always grabs the first item in the list
print(inventory[-1]) # Always grabs the last item in the list

middle = len(inventory) // 2
print(inventory[middle]) # Grabs the middle item in the list (not hard coded)

print("--- Exercise 3: List Slicing ---")
print(inventory[:3]) # Grabs the first three items in the list
print(inventory[-2:]) # Grabs the last two items in the list
print(inventory[::2]) # Grabs every other item in the list


print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # Adds "envelope" to the end of the list
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # Sorts the list in alphabetical order
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # Example coordinates for New York City
# coords[0] = 99 # This will raise a TypeError because tuples are immutable
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")


print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # Empty list to store discounted prices
for price in prices:
    discounted.append(round(price * 0.9, 2)) # Apply a 10% discount and round to 2 decimal places

print(prices)
print(discounted)


print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 290]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
