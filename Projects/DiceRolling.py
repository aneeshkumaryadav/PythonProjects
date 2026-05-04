import random
def calculate_probability(target_sum):
    count = 0
    total_outcomes = 36
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 + die2 == target_sum:
                count += 1
    probability = count / total_outcomes
    return probability
  
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def dice_game():
    target = int(input("Enter a sum between 2 and 12: "))
    if target < 2 or target > 12:
        print("Invalid input! Sum must be between 2 and 12.")
        return
      
    prob = calculate_probability(target)
    print(f"Probability of getting sum {target}: {prob:.4f} ({prob*100:.2f}%)")
    d1, d2 = roll_dice()
    print(f"You rolled: {d1} and {d2} → Sum = {d1 + d2}")
    if d1 + d2 == target:
        print("🎉 You got the target sum!")
    else:
        print("❌ Try again!")

dice_game()
