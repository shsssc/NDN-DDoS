from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.after_request
def add_header(response):
    response.cache_control.max_age = 30000
    return response

if __name__ == "__main__":
    app.run(ssl_context='adhoc')

