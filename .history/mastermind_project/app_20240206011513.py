from flask import Flask, render_template, request
import sys
sys.path.append("/Users/nita/Desktop/DM2/mastermind_project")


app = Flask(__name__)

# Import the game logic functions from mastermind_game.py
from mastermind_game import generate_secret_code, evaluate_guess

# Initialize the secret code when the application starts
secret_code = generate_secret_code()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's guess from the form submission
        user_guess = request.form['user_guess'].upper()

        # Add your game logic here
        correct_color_and_position, correct_color_only = evaluate_guess(secret_code, user_guess)

        if correct_color_and_position == 4:
            result_message = f"Congratulations! You've guessed the code {secret_code}."
        else:
            result_message = f"{correct_color_and_position} correct color and position, {correct_color_only} correct color only."

        return render_template('mastermind_game.html', result=result_message)

    # If it's a GET request, render the initial game board
    return render_template('mastermind_game.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
