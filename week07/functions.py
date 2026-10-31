# Self Assessment Qs:
# 1. The first bug I spotted was the missing colon in the count loop. I immediately found it from the traceback as it was very clear to me and I think that shows that with particular mistake, I can catch it easily.
# 2. In plain English, the apply_discount(price, tier) function takes in a price and a discount tier and returns the price after the discount based on tier has been applied. I think a collegue could definetly use it once they understand how it works. 
# 3. Ai was used on explaining the bugs that appeared in lines 85 and 90/91. The ai definetly helped me build my understanding as it explained why it was wrong.

# Exercise 1

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7% is ${tax1:.2f}")
print(f"Tax for $250 at 8% is ${tax2:.2f}")
print(f"Tax for $350 at 5% is ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

# Defining a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders =[(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} |Total: ${total:.2f}")




# Exercise 6

x = 100 # global x

def double_it():
    # global x  (Dangerous)
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)


# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # To use addition instead of assigning it.
print(f"Total: ${total}")

count = 0
for sale in sales: # Without a colon, theres a syntax error. Added a colon so the count loop works correctly.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Changed from <= to < to avoid IndexError due to having an index that would be previously out of range.
    print(sales[i])
    i += 1