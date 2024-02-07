import random 

def generate_secret_code(): 
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Red, Green, Blue, Yellow, Orange, Purple
    return [random.choice(colors) for _ in range(4)] #enter only 4 colors

def evaluate_guess(secret_code, guess):
    correct_color_and_position = sum(s == g for s, g in zip(secret_code, guess)) 
    #secret guess with correct_color_and_position
    correct_color_only = sum(min(secret_code.count(c), guess.count(c)) for c in set(secret_code)) - correct_color_and_position
     #secret guess with correct_color_only
    return correct_color_and_position, correct_color_only


def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 0

    print("Welcome to Mastermind! Try to guess the 4-color code.")

    while True:
        guess = input("Enter your guess (e.g., RGBY): ").upper()

        if len(guess) != 4 or not all(color in 'RGBYOP' for color in guess):
            print("Invalid input. Please enter a 4-color code using the letters R, G, B, Y, O, P.")
            continue

        attempts += 1

        correct_color_and_position, correct_color_only = evaluate_guess(secret_code, guess)

        if correct_color_and_position == 4:
            print(f"Congratulations! You've guessed the code {secret_code} in {attempts} attempts.")
            break
        else:
            print(f"Attempt {attempts}: {correct_color_and_position} correct color and position, {correct_color_only} correct color only.")

if __name__ == "__main__":
    play_mastermind()