from relay_control import toggle_relay, setup_relay_board_pins
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    cssUrl = url_for('static', filename='style.css')
    print(cssUrl)
    return render_template('home.html', var=3)

if __name__ == '__main__':
    app.run(debug=True)	