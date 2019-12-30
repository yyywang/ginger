# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""
from app.app import create_app

__author__ = "怀月"

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)