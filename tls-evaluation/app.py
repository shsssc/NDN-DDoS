from flask import Flask, request, send_from_directory, make_response

def app_main():
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

    app.run(host='0.0.0.0', port=6000, ssl_context=('rsa-4096-cert.pem', 'rsa-4096-key.pem'))

if __name__ == "__main__":
    app_main()

