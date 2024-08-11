from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    """Display a greeting."""
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Display a greeting to name."""
    return f"Hello {name}"


def covert_celsius(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/f/<float:celsius>')
def convert_temperature(celsius):
    """Display a conversion message of Celsius to Fahrenheit."""
    fahrenheit = covert_celsius(celsius)
    return f"{celsius:.2f} °C = {fahrenheit:.2f} °F"


if __name__ == '__main__':
    app.run()
