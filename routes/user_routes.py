from flask import Blueprint, request, jsonify  
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.login_user(request.get_json()))


@user_bp.route('/listar', methods=['GET'])
def listar_user():
    user_id = get_jwt_identity()
    return jsonify(UserController.listar_user(user_id,request.get_json()))


@user_bp.route('/put/<int:user_id>', methods=['PUT'])
def put_user():
    user_id = get_jwt_identity()
    return jsonify(UserController.put_user(user_id, request.get_json()))

@user_bp.route('/deletar/<int:user_id>', methods=['DELETE'])
def delete_user():
    user_id = get_jwt_identity()
    return jsonify(UserController.delete_user(user_id,request.get_json()))

