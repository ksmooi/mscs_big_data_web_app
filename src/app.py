#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
            }
            label {
                margin-bottom: 8px;
                font-weight: bold;
            }
            input[type="text"] {
                margin-bottom: 16px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 16px;
                width: 95%;
            }
            input[type="submit"] {
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                background-color: #007BFF;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <form action="/echo_user_input" method="POST">
                <label for="name">Name:</label>
                <input name="name" type="text" required>
                <label for="message">Message:</label>
                <input name="message" type="text" required>
                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    name = request.form.get("name", "")
    message = request.form.get("message", "")
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    accept_language = request.headers.get('Accept-Language')
    
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Application</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
                margin: 0 20px;
            }}
            p, ul {{
                text-align: left;
            }}
            .buttons {{
                display: flex;
                justify-content: start;
                margin-top: 20px;
            }}
            .button {{
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                background-color: #007BFF;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
                text-decoration: none;
                text-align: center;
            }}
            .button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p>Name: {name}</p>
            <p>Message: {message}</p>
            <p>Your browser details:</p>
            <ul>
                <li>User Agent: {user_agent}</li>
                <li>IP Address: {ip_address}</li>
                <li>Accept Language: {accept_language}</li>
            </ul>
            <div class="buttons">
                <button class="button" onclick="window.history.back()">Back</button>&nbsp;&nbsp;
                <a href="https://mscs-web-app-8aaa125138dd.herokuapp.com/" class="button">Retry</a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
