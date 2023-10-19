from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index.html', method=['GET'])
def display_form():
    return render_template('index.hmtl')


@app.route('/result.html', method=['POST'])
def process_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        return render_template('result.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
