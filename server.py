from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Roblox Revival is Online!'

@app.route('/login', methods=['POST'])
def login():
    return jsonify({
        "userId": 1,
        "userName": "RevivedUser",
        "displayName": "RevivedUser",
        "authenticationTicket": "FAKE-TICKET-1234"
    })

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return jsonify({
        "Id": user_id,
        "Username": "RevivedUser",
        "DisplayName": "RevivedUser",
        "AvatarUri": "https://yourserver.com/avatar.png"
    })

@app.route('/asset/')
def get_asset():
    return 'Pretend asset data here.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
