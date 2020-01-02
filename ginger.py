# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/30.
"""
from werkzeug.exceptions import HTTPException
from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = "怀月"

app = create_app()

"""
  捕捉所有异常
  1.APIException
  2.HTTPException
  3.Exception
"""
@app.errorhandler(Exception)
def framework_error(e):
    # 处理APIException
    if isinstance(e, APIException):
        return e
    # 处理HTTPException
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    # 处理Exception
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run()