low = 1
high = 100
attempts = 0

print("Think of a number between 1 and 100, and I'll guess it!")
input("Press Enter when you're ready...")

while True:
    guess = (low + high) // 2  
    attempts += 1

    answer = input(f"Is it {guess}? (H = too high, L = too low, C = correct): ")

    if answer == "C":
        print(f"Got it in {attempts} guesses!")
        break
    elif answer == "H":
        high = guess - 1  
    elif answer == "L":
        low = guess + 1  
    else:
        print("Please type H, L, or C.")