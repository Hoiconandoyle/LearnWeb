from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def adminPage():
    return f'Hello Admin'


@app.route('/guest/<guest_name>')
def guestPage(guest_name):
    return f'This is a guest page, hi {guest_name}'


@app.route('/user/<name>')
def redirect_user(name):
    if name == 'admin':
        return redirect(url_for('adminPage'))
    else:
        return redirect(url_for('guestPage', guest_name = name))


if __name__ == "__main__":
    app.run(debug=True)
