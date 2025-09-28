from relay_control import toggle_relay, setup_relay_board_pins, read_relay_state
from flask import Flask, render_template, redirect, url_for, jsonify
from adc import read_mcp3008

app = Flask(__name__)
setup_relay_board_pins(dp=7,lp=11,cp=13)

@app.route('/')
def home():
    cssUrl = url_for('static', filename='style.css')
    print(cssUrl)
    battery_voltage = read_mcp3008(0)
    current_relay_state = read_relay_state()
    return render_template('home.html', house_voltage=battery_voltage, relay_state=current_relay_state)

@app.route('/toggle_relay/<string:relay_id>')
def toggleRoute(relay_id):
    print('toggling')
    toggle_relay(relay_id)
    current_relay_state = read_relay_state()
    print(current_relay_state)
    battery_voltage = read_mcp3008(0)
    return f"Toggled {relay_id}"

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

if __name__ == '__main__':
    app.run(debug=False)