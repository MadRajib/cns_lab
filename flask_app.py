from crypt import methods
from types import MethodDescriptorType
from flask import *

from ciphers.CeaserCipher import CeaserCipher

app = Flask(__name__)

ceaserCipher = CeaserCipher()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# http://127.0.0.1:5000/cns_lab
@app.route("/cns_lab")
def home_page():
    return render_template('home.html')

# Copy below

@app.route("/ceaser_cipher", methods=['POST'])
def ceaser_cipher_page():
    text = request.form.get("text")
    option = request.form.get("option")
    key = request.form.get("key")
    response = ceaserCipher.process_request(text, option, key)
    return jsonify(response)

