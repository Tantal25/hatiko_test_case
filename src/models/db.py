from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from settings import SettingsConfig

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    telegram_id = Column(String, nullable=True, unique=True)
    token = relationship("Token", uselist=False, back_populates='user')


class Token(Base):
    __tablename__ = 'tokens'

    token = Column(String, unique=True)
    token_id = Column(
        Integer, ForeignKey('users.user_id'), unique=True, primary_key=True
    )
    user = relationship('User', back_populates="token")


enigne = create_engine(SettingsConfig.DATABASE_URL)
Session = sessionmaker(bind=enigne)


Base.metadata.create_all(enigne)
