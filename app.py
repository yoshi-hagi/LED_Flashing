from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    mode = request.args.get('mode', 'オフ')
    return render_template('index.html', mode=mode)

@app.route('/led-on', methods=["POST"])
def led_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)
    mode = 'オン'
    return redirect(url_for('index', mode=mode))

@app.route('/led-off', methods=["POST"])
def led_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.LOW)
    mode = 'オフ'
    return redirect(url_for('index', mode=mode))

if __name__ == '__main__':
    app.run(debug=True)