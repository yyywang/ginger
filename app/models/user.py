# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2019/12/31.
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from app.libs.error_code import AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)  # 权限类型，1 代表普通用户
    _password = Column('password', String(1000))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 因为此方法在类User中创建了User实例
    # 所以将此方法定义为静态方法，即：staticmethod
    @staticmethod
    def register_by_email(nickname, account, password):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = password
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email) \
            .first_or_404(description="user not found")
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self.password:
            return False
        return check_password_hash(self.password, raw)

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']
