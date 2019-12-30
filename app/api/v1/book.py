# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""
from flask import Blueprint

from app.libs.redprint import Redprint

book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/v1/book/get')
def get_book():
    return 'i am book'