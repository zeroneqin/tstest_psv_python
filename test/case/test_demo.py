#coding:utf-8

from __future__ import unicode_literals
import logging


from tstest.po.req.demo_req_po import DemoReqPO
from tstest.po.req.demo_req_po_detail import DemoReqPODetail
from tstest.so.demo_so import DemoSO
from tstest.vo.demo_vo import DemoVO

from base_case import BaseCase
from base_suite import  BaseSuite



class TestCase(BaseCase):


    def test_case(self):

        logging.info("Start case")
        demo_req_po_detail = DemoReqPODetail()
        demo_req_po_detail.ip="1.1.1.1"
        demo_req_po = DemoReqPO()
        demo_req_po.user_id=123
        demo_req_po.appkey="demokey123"
        demo_req_po.detail=demo_req_po_detail
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        demo_res_po = DemoSO.send_request_wrapper(BaseSuite.URL,demo_req_po,headers)
        DemoVO.verify(demo_res_po)
        logging.info("End case")