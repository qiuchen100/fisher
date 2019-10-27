"""
    created by 邱晨 on 2019/8/30 11:42 PM.
"""
__author__ = '邱晨'


import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text



