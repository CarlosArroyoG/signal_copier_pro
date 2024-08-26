from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import api_bp
from ..models import User, MT5Account, Signal
from ..database import db
from ..signal_processor import SignalProcessor
from ..mt5_client import MT5Client

@api_bp.route('/signals', methods=['POST'])
@jwt_required()
def create_signal():
    data = request.json
    new_signal = Signal(content=data['content'])
    db.session.add(new_signal)
    db.session.commit()
    
    # Process and execute signal
    processed_signal = SignalProcessor.process_signal(data['content'])
    if processed_signal:
        # Execute signal for all MT5 accounts
        accounts = MT5Account.query.all()
        for account in accounts:
            MT5Client.initialize(account.login, account.password, account.server)
            MT5Client.place_order(**processed_signal)
            MT5Client.shutdown()
    
    return jsonify({'message': 'Signal created and processed successfully'}), 201

@api_bp.route('/mt5_accounts', methods=['GET'])
@jwt_required()
def get_mt5_accounts():
    user_id = get_jwt_identity()
    accounts = MT5Account.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': a.id, 'login': a.login, 'server': a.server} for a in accounts]), 200

@api_bp.route('/mt5_accounts', methods=['POST'])
@jwt_required()
def add_mt5_account():
    user_id = get_jwt_identity()
    data = request.json
    new_account = MT5Account(user_id=user_id, login=data['login'], password=data['password'], server=data['server'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'MT5 account added successfully'}), 201