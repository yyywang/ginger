# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""

from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('', methods=['GET'])
def get_book():
    return 'i am book'

@api.route('', methods=['POST'])
def create_book():
    return 'create book'