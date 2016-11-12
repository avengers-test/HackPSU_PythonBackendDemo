#Code based on presentation by Josh Li and Mayank Makwana at HackPSU 2016
#https:github.com/

from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello World'

@application.route('/api/getroute', methods=['GET'])
def api_getroute():
    args = request.args
    output = {
        'sum': int(args['x']) + int(args['y']),
        'product': int(args['x']) * int(args['y'])
    }
    return jsonify(output)

if __name__ == "__main__":
    application.run(debug=True)
