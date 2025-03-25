#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print String Route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Display in browser

# 3. Count Route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    return '\n'.join(str(num) for num in numbers) + '\n'  # Ensure each number appears on a new line

# 4. Math Operations Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Return 400 error for invalid operation
    return str(result)  # Convert result to string for browser display

if __name__ == '__main__':
    app.run(port=5555, debug=True)
