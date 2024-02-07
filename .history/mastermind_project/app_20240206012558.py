# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mastermind_game.html')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    user_guess = request.json.get('guess')

    # Process the user's guess (use your existing game logic)
    # For demonstration purposes, just sending a simple response
    response_data = {'message': f'You submitted: {user_guess}'}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
