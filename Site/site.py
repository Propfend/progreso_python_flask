from flask import Flask
from flask import render_template
site = Flask(__name__)

@site.route('/', defaults={'nome':None})
@site.route('/ola/<nome>')
def ola(nome):
    return render_template('index.html', nome=nome)

if __name__ == '__main__':
    site.run(debug=True, port=3000)
