# Q1. Explain GET and POST methods.

'''GET Method:
The GET method is used to request data from a specified resource on the web. 
When a client (like a browser) sends a GET request, it is essentially asking the
server to return some data.A GET request appends data to the URL, making it visible 
to anyone who has access to the URL.'''

'''Key characteristics:
Idempotent: A GET request should not have any side effects (e.g., modifying data 
on the server). Repeated GET requests should yield the same result.

Data in URL: Parameters (if any) are included in the URL after a question mark ?
and are visible to anyone who has access to the URL. Example: GET /search?query=python.

Caching: GET requests can be cached by browsers, which may lead to faster response
times.

Limited data size: Since the data is sent via URL, GET requests are limited by the
length of the URL, which is typically around 2000 characters.'''

'''POST Method:
The POST method is used to send data to the server to create or update a resource.
It is commonly used when submitting form data, uploading files, or sending more 
complex data.'''

'''Key characteristics:

Non-idempotent: A POST request may change the state of the server (e.g., creating 
a new user or updating a database).

Data in body: The data is included in the body of the request, not in the URL. This 
makes it more secure compared to GET, as sensitive data isn't exposed in the URL.

No size limit: POST requests can handle large amounts of data, making them 
suitable for file uploads or complex data submissions.

Not cached: POST requests are not cached by default.'''


'''When to use each method:

Use GET when retrieving data without causing any changes to the server or database.
For example, viewing a webpage or fetching results from a search engine.


Use POST when sending data that modifies the server's state, like submitting a form, 
logging in, or uploading a file.'''


'''Example:
GET:
Used when the user is requesting information from the server, like navigating to 
a webpage or retrieving search results. The request might look like:

GET /profile?id=123


POST:
Used when submitting data that will modify the server’s state, such as logging in
or submitting a form.
Example:POST /login'''



 #Q2. Why is request used in Flask?

'''In Flask, the request object is used to handle incoming data from HTTP requests.
It provides access to all the information sent by the client (e.g., a browser or
 another server) in an HTTP request. This allows the server to interact with the
data submitted by the client, whether it’s in the form of URL parameters, form data,
cookies, headers, or JSON.'''

'''Here are some key reasons why request is important in Flask:

1. Accessing Request Data:
The request object provides methods to access various parts of the incoming request:

Form Data: When a client submits a form, request.form allows access to the submitted form
data (using POST method).

URL Parameters: With GET requests, parameters can be accessed via request.args.

JSON Payload: If the client sends JSON data, it can be accessed using request.get_json().

Headers and Cookies: The request.headers and request.cookies attributes allow access to
request headers and cookies, respectively.'''

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

'''@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return "Submit Page!"
    # Process form data for POST request
    return redirect(url_for('thank_you'))


if __name__ == '__main__':
    app.run(debug=True)'''


