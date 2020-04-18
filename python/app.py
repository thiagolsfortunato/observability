import os
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

node_host = os.getenv("NODE_HOST", default = "localhost")
node_port = os.getenv("NODE_PORT", default = "3000")

html = """ 
<h3>Type your message:</h3> 
<br>
<form method='POST' action='/'>
    <input type='text' name='message'>
    <input type='submit'>
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get("message")
        app.logger.info(message)
        resp = save_message(message)
        return resp
    return html

def save_message(message):
    NODE_API = "http://" + node_host + ":" + node_port + "/save"
    resp = requests.post(url = NODE_API, data = {'message': message})
    print(resp.text)
    if (resp):
        response = """
        <h3>{resp}</h3>
        <button onClick="window.location.href=window.location.href;">Reload</button>
        """.format(resp=resp.text)
    return response
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
