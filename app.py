from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html', name=" World")


@app.route('/<name>')
def default_page(name):
    return render_template('index.html', name=" World")


@app.route('/test', methods=['GET', 'POST'])
def test_name():
    print(request.method)
    if request.method == 'GET':
        return render_template('name.html')
    else:
        name = str(request.form['data'])
        return render_template('index.html', name=(', ' + name.title()))


if __name__ == '__main__':
    app.debug = True
    app.run()
