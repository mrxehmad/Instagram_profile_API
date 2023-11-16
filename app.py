from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route('/get_profile_pic', methods=['GET'])
def get_profile_pic():
    username = request.args.get('username')

    if not username:
        return jsonify({'error': 'Username parameter is missing.'}), 400

    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        profile_pic_url = profile.profile_pic_url

        return jsonify({'username': username, 'profile_pic_url': profile_pic_url})

    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({'error': 'User does not exist.'}), 404

@app.route('/', methods=['GET'])
def error_message():
    return jsonify({'error': 'Invalid API endpoint. Use /get_profile_pic?username=<username>'}), 400

if __name__ == '__main__':
    app.run(debug=False, port=80)
