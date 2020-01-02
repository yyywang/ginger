# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/31.
"""
# 400 表请求参数错误
# 401 未授权
# 403 禁止访问
# 404 未找到资源/页面
# 500 服务器产生未知错误
# 200 查询成功
# 201 创建/更新成功
# 204 删除成功
# 301 重定向
from app.libs.error import APIException

class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*=^=)!'
    error_code = 999

class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006

class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

