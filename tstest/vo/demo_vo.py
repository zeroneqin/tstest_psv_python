#coding:utf-8

from __future__ import unicode_literals
import logging
import requests
import jsonstruct

class DemoVO(object):

    @classmethod
    def verify(cls, demo_res_po):
        status_code = demo_res_po.status_code
        if  status_code != 200:
            logging.error("Fail, 预期HTTP状态s:[%d], 实际状态:[%d]",200,status_code)
        assert status_code == 200

        userId = demo_res_po.userId
        if userId !=0:
             logging.error("Fail,预期error code:[%d], 实际[%d]",0,code)
        assert userId == 0
