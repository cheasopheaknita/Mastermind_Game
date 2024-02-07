# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_secret_code():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    return [random.choice(colors) for _ in range(4)]

def evaluate_guess(secret_code, guess):
    correct_color_and_position = sum(s == g for s, g in zip(secret_code, guess))
    correct_color_only = sum(min(secret_code.count(c), guess.count(c)) for c in set(secret_code)) - correct_color_and_position
    return correct_color_and_position, correct_color_only

secret_code = generate_secret_code()

@app.route('/')
def index():
    return render_template('mastermind_game.html', secret_code=secret_code)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    user_guess = request.json.get('guess')

    # Validate the guess here if needed
    if len(user_guess) != 4 or not all(color in 'RGBYOP' for color in user_guess):
        return jsonify({'error': 'Invalid input. Please enter a 4-color code using the letters R, G, B, Y, O, P.'})

    correct_color_and_position, correct_color_only = evaluate_guess(secret_code, user_guess)

    if correct_color_and_position == 4:
        result_message = f"Congratulations! You've guessed the code {secret_code}."
    else IF:
        result_message = f"Correct color and position: {correct_color_and_position}, Correct color only: {correct_color_only}."

    return jsonify({'result': result_message})

if __name__ == '__main__':
    app.run(debug=True)
