from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for adding a message
@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form.get('message')
    # Here you would normally save the message to a database or process it
    return render_template('message.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
