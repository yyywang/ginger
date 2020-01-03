# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""
from flask import jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(ident=uid,
                                 description='user not found')
    return jsonify(user)