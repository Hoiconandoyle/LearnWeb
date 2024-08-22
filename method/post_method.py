from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return f'Welcome {name} to this page'


@app.route('/admin')
def adminPage():
    return "This an Admin web page"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        if user.lower() == 'admin@gmail.com':
            return redirect(url_for('adminPage'))
        elif user.lower() == '':
            return "You can enter user name"
        else:
            return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
