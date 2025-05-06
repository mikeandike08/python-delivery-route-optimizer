from queue import Empty
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from werkzeug.utils import secure_filename
from DOA import routeCalc
import os

app = Flask(__name__)
app.secret_key = "VerySecretKey"

coords = []

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def home():
    global coords
    coords = [] # Resets coords each load
    return render_template('homepage.html')

@app.route("/submit", methods=["POST", "GET"])
def submit():
    global coords
    coords = []
    data = request.form.get('input_form')
    filename = session.get('file')
    if filename and not data:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        with open(filepath, 'r') as f:
            data = f.read()

    address_list = [addr.strip() for addr in data.split(',') if addr.strip() != '']

    session['addresses'] = address_list

    return render_template('route.html', addresses=address_list)

@app.route("/calculate", methods=["GET"])
def calcRoute():
    global coords

    address_list = session.get('addresses')
    use_tsp = request.args.get('use-tsp') == 'on' # returns True if checked
    print(use_tsp)

    coords = routeCalc.getAddressPoints(address_list, coords, use_tsp)

    print("Coords sent to map:", coords)
    if not coords:
        return "No coordinates available", 400
    return render_template('map.html', coords=coords)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session["file"] = filename
        return redirect(url_for('submit'))
    return "INVALID FILE", 400

@app.route('/howto', methods=['GET'])
def howto():
    return render_template('howto.html')

if __name__ == "__main__":
    app.run(debug=False)