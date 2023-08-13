from flask import Flask
from flask import render_template


site = Flask('__name__')


@site.route('/')
def ola():
    return 'ola'


if __name__ == '__main__':
    site.run(debug=True, port=3000)

