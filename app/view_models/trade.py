# -*- coding: UTF-8 -*-
"""
    created by 邱晨 on 2020/01/24 10:42 PM.
"""
__author__ = '邱晨'


class TradeViewModel:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(good) for good in goods]

    def __map_to_trade(self, good):
        time = good.create_datetime.strftime(
            '%Y-%m-%d') if good.create_datetime else '未知'
        return dict(
            user_name=good.user.nickname,
            time=time,
            id=good.id
        )
