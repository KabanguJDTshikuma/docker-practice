# from fastapi import FastAPI
# from pydantic import BaseModel
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    endpoint = "http://139.162.246.62:8001/"
    r = requests.get(endpoint)
    print(r.status_code)
    print(r.json())

    return render_template('index.html', results=r.json())



if __name__ == '__main__':
    app.run(debug=True)
