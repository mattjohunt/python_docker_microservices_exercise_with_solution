from application import app
import requests

@app.route('/data')
def book():
    URL = "http://dataapi:5000"

    r = requests.get(URL)

    return r.text
