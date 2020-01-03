# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/31.
"""
from flask import request
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint("client")

@api.route('/register', methods=['POST'])
def create_client():
    # 如果校验不通过会抛出异常，后面的代码就不执行了
    form = ClientForm().validate_for_api()
    # 根据不同的客户端执行不同的注册程序
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        ClientTypeEnum.USER_MINA: __register_user_by_mina
    }
    promise[form.type.data]()
    # 如果校验不通过，抛出异常
    # 编码原则：我们可以接受定义时的复杂，但不能接受调用时候的复杂。
    # 因为定义只定义一次，而调用会有很多次
    return Success()

def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                            form.account.data,
                            form.secret.data)

def __register_user_by_mina():
    pass