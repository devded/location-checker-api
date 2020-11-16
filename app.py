from flask import Flask, jsonify
import apidata

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return "<h1> Deployed to Heroku</h1>"

@app.route('/api')
def api():
    data = apidata.getdata()
    return jsonify(data)


if __name__ == "__main__":
    app.run()