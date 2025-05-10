from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
