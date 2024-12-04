from flask import Flask, render_template

app = Flask(__name__)

@app.route('/greet/<username>')
def greet_user(username):
    return render_template('greet.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)