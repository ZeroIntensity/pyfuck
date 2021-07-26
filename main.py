from flask import Flask, render_template, request
import compiler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        read = request.form.get('read')
        compiled = compiler.compile(read)

        return render_template('index.html', txt = compiled)

    return render_template('index.html', txt = 'exec(f"")')


app.run('localhost', 5000)