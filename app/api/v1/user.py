# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""
from flask import Blueprint

from app.libs.redprint import Redprint

user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('/v1/user/get')
def get_user():
    return 'i am user'