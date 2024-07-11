#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    accept_language = request.headers.get('Accept-Language')
    
    return f'''
        <p>You entered: {input_text}</p>
        <p>Your browser details:</p>
        <ul>
            <li>User Agent: {user_agent}</li>
            <li>IP Address: {ip_address}</li>
            <li>Accept Language: {accept_language}</li>
        </ul>
        '''

if __name__ == "__main__":
    app.run(debug=True)
