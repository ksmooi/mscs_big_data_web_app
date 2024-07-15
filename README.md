# Build Web Application with Flask and Heroku

This project is a simple web application built with Flask and deployed on Heroku. It provides a form where users can input their name and a message, and upon submission, it displays the input along with some browser details.

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Virtualenv

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ksmooi/mscs_web_app_flask_heroku.git
   cd mscs_web_app_flask_heroku
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```sh
   pip install Flask
   ```

4. **Set the Flask application environment variable:**
   ```sh
   export FLASK_APP=src/app.py
   ```

### Running the Application

1. **Navigate to the source directory:**
   ```sh
   cd src
   ```

2. **Run the Flask application:**
   ```sh
   flask run
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

### Directory Structure

```
mscs_web_app_flask_heroku/
├── src/
│   └── app.py
├── venv/
├── .gitignore
└── README.md
```

### Deploying to Heroku

1. **Login to Heroku:**
   ```sh
   heroku login
   ```

2. **Create a new Heroku application:**
   ```sh
   heroku create mscs-web-app-flask-heroku
   ```

3. **Add Heroku as a remote repository:**
   ```sh
   git remote add heroku https://git.heroku.com/mscs-web-app-flask-heroku.git
   ```

4. **Create a `Procfile` in the root directory with the following content:**
   ```
   web: flask run
   ```

5. **Deploy the application:**
   ```sh
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku main
   ```

   The application will be accessible at the URL provided by Heroku.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Deploying Flask to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Example Flask Application](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)

