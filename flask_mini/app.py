from flask import Flask, render_template, request,  jsonify, url_for



app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/status')
def status():
    return jsonify({'status': 'OK'}), 200

@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        data = request.get_json()
        return jsonify(data), 201
    else:
        return jsonify({"error": "Invalid data"}), 400

app.run(host="0.0.0.0" ,debug=True)