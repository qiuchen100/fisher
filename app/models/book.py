# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2019/10/27 11:42 PM.
"""
from sqlalchemy import Column, Integer, String, FLOAT
from app.models.base import db, Base

__author__ = '邱晨'


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='佚名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(FLOAT)
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
