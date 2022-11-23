from crypt import methods
from types import MethodDescriptorType
from flask import *

from ciphers.CeaserCipher import CeaserCipher
from ciphers.AffineCipher import AffineCipher
from ciphers.VigenereCipher import VigenereCipher
from ciphers.PlayfairCipher import PlayfairCipher

# TODO: import new cipher
# from ciphers.NewCipher import NewCipher

app = Flask(__name__)

ceaserCipher = CeaserCipher()
affineCipher = AffineCipher()
vigenereCipher = VigenereCipher()
playfairCipher = PlayfairCipher()

# TODO: init new class
# newCipher = NewCipher()

@app.route("/")
def hello_world():
    return render_template('home.html')

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

@app.route("/affine_cipher", methods=['POST'])
def affine_cipher_page():
    text = request.form.get("text")
    option = request.form.get("option")
    key_1 = int(request.form.get("key_1"))
    key_2 = int(request.form.get("key_2"))
    response = affineCipher.process_request(text, option, [key_1,key_2])
    return jsonify(response)

@app.route("/vigenere_cipher", methods=['POST'])
def vigenere_cipher_page():
    text = request.form.get("text")
    option = request.form.get("option")
    key = request.form.get("key")
    response = vigenereCipher.process_request(text, option, key)
    return jsonify(response)

@app.route("/playfair_cipher", methods=['POST'])
def playfair_cipher_page():
    text = request.form.get("text")
    option = request.form.get("option")
    key = request.form.get("key")
    response = playfairCipher.process_request(text, option, key)
    return jsonify(response)


# TODO: add new end point
# @app.route("/new_cipher", methods=['POST'])
# def new_cipher_page():
#     text = request.form.get("text")
#     option = request.form.get("option")
#     key = request.form.get("key")
#     response = newCipher.process_request(text, option, key)
#     return jsonify(response)