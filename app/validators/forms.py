# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/31.
"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form

class ClientForm(Form):
    # 自定义错误信息
    account = StringField(validators=[DataRequired(message="不允许为空"), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            # 判断用户传过来的数字是否是枚举类型的一种】
            # 将数字转换为枚举类型，可读性强
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[
        DataRequired(),
        # 密码只能包含字母、数字和下划线
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[
        DataRequired(),
        length(min=2, max=22)
    ])

    # 校验邮箱是否已被注册
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message="账号已注册")