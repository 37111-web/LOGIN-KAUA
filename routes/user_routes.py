from flask import Blueprint, request, jsonify  
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.login_user(request.get_json()))

@user_bp.route('/register', methods=['GET'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['GET'])
def login():
    return jsonify(UserController.login_user(request.get_json()))

@user_bp.route('/register', methods=['PUT'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['PUT'])
def login():
    return jsonify(UserController.login_user(request.get_json()))


@user_bp.route('/register', methods=['DELETE'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['DELETE'])
def login():
    return jsonify(UserController.login_user(request.get_json()))

