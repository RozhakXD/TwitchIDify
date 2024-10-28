from app import app
from flask import render_template
from flask import jsonify

@app.route('/api/twitch/<username>', methods=['GET'])
def twitch(username):
    from app.twitch import get_id_twitch

    return jsonify(
        get_id_twitch(username)
    )

@app.route('/')
def index():
    return render_template('index.html')