import random

def generate_secret_code():
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    return [random.choice(colors) for _ in range(4)]

def evaluate_guess(secret_code, user_guess):
    correct_color_and_position = sum(a == b for a, b in zip(secret_code, user_guess))
    correct_color_only = sum(min(secret_code.count(color), user_guess.count(color)) for color in set(user_guess)) - correct_color_and_position
    return correct_color_and_position, correct_color_only

def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 0

    while attempts < 10:
        user_guess = input("Enter your guess (e.g., red blue green yellow): ").split()
        
        if len(user_guess) != 4 or any(color.lower() not in ['red', 'blue', 'green', 'yellow', 'orange', 'purple'] for color in user_guess):
            print("Invalid input. Please enter a valid guess.")
            continue

        attempts += 1
        result = evaluate_guess(secret_code, user_guess)

        print(f"Result: {result[0]} correct color and position, {result[1]} correct color only.")

        if result[0] == 4:
            print(f"Congratulations! You've guessed the secret code: {secret_code}")
            break

    if attempts == 10:
        print(f"Sorry, you've reached the maximum number of attempts. The secret code was: {secret_code}")

if __name__ == "__main__":
    play_mastermind()
