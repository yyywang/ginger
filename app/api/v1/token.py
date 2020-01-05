# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/1/3.
"""
from flask import current_app, jsonify
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    # 用序列化器生成的Token不是普通的字符串
    # 需要调用decode转码
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """
    生成令牌
    :param uid: identity of user 
    :param ac_type: client type
    :param scope: auth scope
    :param expiration: expiration time
    :return: 
    """
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    # 调用序列化器的dumps方法将需要写入的信息以字典形式写入Token中
    # 返回值为字符串
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })