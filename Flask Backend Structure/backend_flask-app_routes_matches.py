from flask import Blueprint, request, session, jsonify

matches_bp = Blueprint('matches', __name__)

@matches_bp.route('/api/like', methods=['POST'])
def like_profile():
    data = request.get_json()
    profile_id = data.get('profile_id')
    
    if 'likes' not in session:
        session['likes'] = []
    
    session['likes'].append(profile_id)
    session.modified = True
    
    return jsonify({'status': 'success', 'message': 'Profile liked!'})

@matches_bp.route('/api/dislike', methods=['POST'])
def dislike_profile():
    data = request.get_json()
    profile_id = data.get('profile_id')
    
    if 'dislikes' not in session:
        session['dislikes'] = []
    
    session['dislikes'].append(profile_id)
    session.modified = True
    
    return jsonify({'status': 'success', 'message': 'Profile disliked!'})
