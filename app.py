from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.route("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """

    # first_name = request.args.get('first_name')
    # second_name = request.args.get('second_name')

    # if first_name and second_name:
    #     response = {"data": f"Is your name {first_name} {second_name}"}
    # elif first_name:
    #     response = {"data": f"Hello, {first_name}!"}
    # elif second_name:
    #     response = {"data": f"Hello Mr {second_name}!"}
    # else:
    #     response = {"status": "error"}

    response = {"data": "Hello, World!"}
    return jsonify(response)