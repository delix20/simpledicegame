import random

# Parameters
rolls = 20  # number of times to roll the dice
dice_sides = 6  # number of sides on the dice
target_number = 6  # the number we're looking for

count_target = 0  # counter for target number

print(f"Rolling a {dice_sides}-sided dice {rolls} times...")
print(f"Counting how many times we get a {target_number}:\n")

for i in range(1, rolls + 1):
    # Generate a random number between 1 and dice_sides
    roll = random.randint(1, dice_sides)
    print(f"Roll {i}: {roll}")
    
    # Check if we got the target number
    if roll == target_number:
        count_target += 1

print(f"\nResult: Got {target_number} a total of {count_target} times out of {rolls} rolls.")
print(f"Percentage: {(count_target / rolls) * 100:.1f}%")