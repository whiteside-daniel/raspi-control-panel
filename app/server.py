from relay_control import toggle_relay, setup_relay_board_pins
from flask import Flask, render_template, url_for, jsonify
from adc import read_mcp3008

app = Flask(__name__)
setup_relay_board_pins(dp=7,lp=11,cp=13)

@app.route('/')
def home():
    cssUrl = url_for('static', filename='style.css')
    print(cssUrl)
    battery_voltage = read_mcp3008(0)
    return render_template('home.html', house_voltage=battery_voltage)

@app.route('/toggle_relay/<string:relay_id>')
def toggleRoute(relay_id):
    print('toggling')
    toggle_relay(relay_id)
    return f' Relay {relay_id}'

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

if __name__ == '__main__':
    app.run(debug=False)