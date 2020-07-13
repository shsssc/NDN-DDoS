from flask import Flask, request, send_from_directory, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/cachable/<path:path>')
def send_static(path):
    response= make_response( send_from_directory('static', path))
    response.cache_control.max_age = 4321
    return(response)

@app.route('/dynamic/<path:path>')
def send_dynamic(path):
    response= make_response( send_from_directory('dynamic', path))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    #response.headers['Cache-Control'] = 'public, max-age=0'
    return(response)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
