from flask import Flask, request

app = Flask(__name__)  # Create Flask instance

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        username = request.form.get('username', 'Guest')  # Retrieve the username from the form
        return f"Hello, {username}!"
    else:  # Handle GET requests
        return '''
            <form action="/submit" method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username">
                <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)