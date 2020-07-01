from scraper import my_url
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def func():
    return 
    
@app.route("/api/")
def my_url1():
    return jsonify(my_url())
    


if __name__ == "__main__":
    app.run(host='127.10.10.0', port=5000) 