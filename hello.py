from flask import Flask
app = Flask(__name__)


@app.route('/mycv/<name>')
def profile(name):
    return f'Chao em {name},  anh dung day tu chieu'


@app.route('/age/<float:age>')
def age_profile(age):
    return f'Tuoi cua ban la {age}'


if __name__ == "__main__":
    app.run(debug=True)
