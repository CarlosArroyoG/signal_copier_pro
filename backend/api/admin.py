from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import api_bp
from ..models import User, MT5Account
from ..database import db

@api_bp.route('/admin/users', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user = User.query.get(get_jwt_identity())
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users]), 200

@api_bp.route('/admin/mt5_accounts', methods=['GET'])
@jwt_required()
def get_all_mt5_accounts():
    current_user = User.query.get(get_jwt_identity())
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    accounts = MT5Account.query.all()
    return jsonify([{'id': a.id, 'user_id': a.user_id, 'login': a.login, 'server': a.server} for a in accounts]), 200

@api_bp.route('/admin/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user = User.query.get(get_jwt_identity())
    if not current_user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403
    
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404