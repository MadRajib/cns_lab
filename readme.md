## To install
```bash
# make the bash script as executable
$ chmod +x run.sh
```
## To run
```
$ ./run.sh
```
## To add a new chiper
1. create a cipher file insife cipher folder (take CeaserChiper.py as reference)
2. import the cipher in flask_app.py
```python
from ciphers.newCipher import newCipher #add this

....

newCipher = newCipher() # add this
```
3. create the endpoint in flask_app.py
```python
@app.route("/new_cipher", methods=['POST']) # add this
def ceaser_cipher_page():
    text = request.form.get("text")
    option = request.form.get("option")
    key = request.form.get("key")
    response = newCipher.process_request(text, option, key)
    return jsonify(response)
```
4. create a form in home.html file for the chiper inside div with class cipher-forms
```html
<div id="new_cipher_body">  // add this
            <form  action={{url_for('new_cipher_page')}}>  //add this
                <div class="form-group">
                    <label for="inputText">Text</label>
                    <textarea type="text" name="text" class="form-control" id="inputText" placeholder="Type Text"></textarea>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="inputOption">Option</label>
                        <select name="option" id="inputOption" class="form-control">
                            <option selected value="1">Encrypt</option>
                            <option value="2">Decrypt</option>
                        </select>
                    </div>
                    <div class="form-group col-md-6">
                        <label for="inputKey">Key</label>
                        <input name="key" type="text" class="form-control" id="inputKey" placeholder="1..26">
                    </div>
                </div>
                <button  type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
```
5. add the cipher in dropdown chiper list
```html
                    <div class="dropdown-menu" id="cipher-dropdown-menu" aria-labelledby="dropdownMenuButton">
                        <a class="dropdown-item" href='#'>Ceaser Cipher</a>
                        <a class="dropdown-item" href="#">Vigelence Cipher</a>
                        <a class="dropdown-item" href="#">New Chiper</a>
                    </div>
```
