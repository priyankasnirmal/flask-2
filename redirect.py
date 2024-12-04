#Q3. Why is redirect() used in Flask?

'''In Flask, the redirect() function is used to direct users to a different endpoint or URL.
It is particularly useful when you want to dynamically change the flow of an application, 
such as after a form submission, when handling authentication, or when implementing routes
that transition between different parts of your app.'''

'''Key Use Cases of redirect():

Redirect After Form Submission: After processing a form submission, it's common to redirect
the user to another page (e.g., a confirmation page) to follow the Post/Redirect/Get (PRG)
pattern. This helps prevent issues like duplicate form submissions if the user refreshes 
the page.'''




from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Go to /submit to submit your form."

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # Redirecting to a thank-you page after the form submission
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the form!"

if __name__ == '__main__':
    app.run(debug=True)
